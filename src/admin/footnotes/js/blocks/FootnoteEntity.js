import PropTypes from 'prop-types';
const Component = window.React.Component;
const Icon = window.wagtail.components.Icon;
const TooltipEntity = window.draftail.TooltipEntity;
const ICON = <Icon name="asterisk" className="asterisk" />;
const shortid = require('shortid');
const $ = window.jQuery;

const getAttributes = (data) => {
    const icon = ICON;
    const label = data.text || null;

    return {
        icon,
        label,
    };
};

window.footnoteUUIDList = window.footnoteUUIDList || {};

const checkExistingUUID = (entityKey, uuid) => {

    // check that this uuid doesn't already exist (which would happen with a copy/paste action)
    let verifiedUUID;

    if (typeof window.footnoteUUIDList[uuid] === 'undefined') {
        verifiedUUID = uuid;
    } else if (window.footnoteUUIDList[uuid] !== entityKey) {
        verifiedUUID = shortid.generate();
    } else if (window.footnoteUUIDList[uuid] === entityKey) {
        verifiedUUID = uuid;
    }

    window.footnoteUUIDList[verifiedUUID] = entityKey;
    return verifiedUUID;
}

const handleUUID = (lastChangeType, contentState, entityKey, data) => {

    let verifiedUUID = data.uuid;

    if (lastChangeType === 'insert-fragment') {
        verifiedUUID = checkExistingUUID(entityKey, data.uuid);
    } else {
        window.footnoteUUIDList[verifiedUUID] = entityKey;
    }

    contentState.replaceEntityData(
        entityKey,
        {
            text: data.text,
            uuid: verifiedUUID
        }
    );
}

export class FootnoteEntity extends Component {
    constructor(props) {
        super(props);

        const {
            contentState,
            entityKey,
        } = this.props;
    }

    render() {
        const {
            contentState,
            entityKey,
        } = this.props;

        const lastChangeType = this.props.getEditorState().getLastChangeType();

        this.props.children = '';
        const data = contentState.getEntity(entityKey).getData();
        handleUUID(lastChangeType, contentState, entityKey, data);

        // TODO: find a way to set the 'showTooltipAt' state of the tooltip entity properly
        // This .hide() instruction is here as the tooltip entity appears on sibling entities when a footnote is removed
        $('.Tooltip.Tooltip--top').hide();

        return (
            <span
                role="button"
                className="FootnoteEntity"
            >
                <TooltipEntity
                    {...this.props}
                    {...getAttributes(data)}
                />
            </span>
        );
    }
}

FootnoteEntity.propTypes = {
    entityKey: PropTypes.string.isRequired,
    children: PropTypes.node.isRequired,
};
