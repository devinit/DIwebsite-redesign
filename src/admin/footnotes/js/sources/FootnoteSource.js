import PropTypes from 'prop-types';
const Component = window.React.Component;
const Modifier = window.DraftJS.Modifier;
const RichUtils = window.DraftJS.RichUtils;
const EditorState = window.DraftJS.EditorState;
const ENTITY_TYPE = window.Draftail.ENTITY_TYPE;
import { FOOTNOTE_CHOOSER_MODAL_ONLOAD_HANDLERS } from '../footnote-chooser-modal';
import { getSelectionText } from '../DraftUtils';
const shortid = require('shortid');
const $ = window.jQuery;

const { STRINGS } = window.wagtailConfig.STRINGS;
const FOOTNOTE = 'FOOTNOTE';
const MUTABILITY = {};
MUTABILITY[FOOTNOTE] = 'IMMUTABLE';

export const getChooserConfig = (entityType, entity, selectedText) => {
    let url;
    let urlParams;
    switch (entityType.type) {
        case FOOTNOTE:
            urlParams = {
                text: selectedText,
                uuid: shortid.generate(),
            };

            if (entity) {
                const data = entity.getData();
                if (data.text) {
                     urlParams.text = data.text;
                }
                if (data.uuid) {
                     urlParams.uuid = data.uuid;
                }
            }

            return {
                url: '/admin/footnotes/chooser/',
                urlParams: urlParams,
                onload: FOOTNOTE_CHOOSER_MODAL_ONLOAD_HANDLERS,
            };

        default:
            return {
                url: null,
                urlParams: {},
                onload: {},
            };
    }
};

export const filterEntityData = (entityType, data) => {
    switch (entityType.type) {
    case FOOTNOTE:
        return {
            text: data.text,
            uuid: data.uuid,
        };
    default:
        return {};
    }
};

/**
 * Interfaces with Wagtail's ModalWorkflow to open the chooser,
 * and create new content in Draft.js based on the data.
 */
class FootnoteSource extends Component {
    constructor(props) {
        super(props);
        this.onChosen = this.onChosen.bind(this);
        this.onClose = this.onClose.bind(this);
    }

    componentDidMount() {
        const { onClose, entityType, entity, editorState } = this.props;
        const selectedText = getSelectionText(editorState);
        const { url, urlParams, onload } = getChooserConfig(entityType, entity, selectedText);

        $(document.body).on('hidden.bs.modal', this.onClose);

        // eslint-disable-next-line new-cap
        this.workflow = global.ModalWorkflow({
            url,
            urlParams,
            onload,
            responses: {
                footnoteChosen: (data) => this.onChosen(data),
            },
            onError: () => {
                // eslint-disable-next-line no-alert
                window.alert(STRINGS.SERVER_ERROR);
                onClose();
            },
        });
    }

    componentWillUnmount() {
        this.workflow = null;
        $(document.body).off('hidden.bs.modal', this.onClose);
    }

    onChosen(data) {
        const { editorState, entityType, onComplete } = this.props;
        const content = editorState.getCurrentContent();
        const selection = editorState.getSelection();

        const entityData = filterEntityData(entityType, data);
        const mutability = MUTABILITY[entityType.type];
        const contentWithEntity = content.createEntity(entityType.type, mutability, entityData);
        const entityKey = contentWithEntity.getLastCreatedEntityKey();

        let nextState;

        // Replace text if the chooser demands it, or if there is no selected text in the first place.
        const shouldReplaceText = data.text || selection.isCollapsed();

        if (shouldReplaceText) {
            const newText = data.text;
            const newContent = Modifier.replaceText(content, selection, newText, null, entityKey);
            nextState = EditorState.push(editorState, newContent, 'insert-characters');
        }
        else {
            nextState = RichUtils.toggleLink(editorState, selection, entityKey);
        }

        // IE11 crashes when rendering the new entity in contenteditable if the modal is still open.
        // Other browsers do not mind. This is probably a focus management problem.
        // From the user's perspective, this is all happening too fast to notice either way.
        this.workflow.close();

        onComplete(nextState);
    }

    onClose(e) {
        const { onClose } = this.props;
        e.preventDefault();

        onClose();
    }

    render() {
        return null;
    }
}

FootnoteSource.propTypes = {
    editorState: PropTypes.object.isRequired,
    entityType: PropTypes.object.isRequired,
    entity: PropTypes.object,
    onComplete: PropTypes.func.isRequired,
    onClose: PropTypes.func.isRequired,
};

FootnoteSource.defaultProps = {
    entity: null,
};

export default FootnoteSource;
