// From http://docs.wagtail.io/en/v2.0/advanced_topics/customisation/extending_draftail.html#creating-new-entities with modifications
// Included into the CMS via home/wagtail_hooks.py, this file adds a custom button into the rich text editor.
// This button creates two prompt windows, one which asks for text and another for an link.
// Using those two pieces of information, an <a> element with href equal to link is created.
// If the user has highlighted some text prior to clicking the button, the text prompt is automatically filled.

// const React = window.React;
// const Modifier = window.DraftJS.Modifier;
// const EditorState = window.DraftJS.EditorState;

class NonModalLinkSource extends React.Component {
  componentDidMount() {
    const { editorState, entityType, onComplete } = this.props;

    const content = editorState.getCurrentContent();
    const selection = editorState.getSelection();
    const anchorKey = selection.getAnchorKey();
    const currentContent = editorState.getCurrentContent();
    const currentBlock = currentContent.getBlockForKey(anchorKey);
    const start = selection.getStartOffset();
    const end = selection.getEndOffset();
    const selectedText = currentBlock.getText().slice(start, end);

    const linkText = window.prompt('Link display text', selectedText);

    if (linkText) {
      const linkHref = window.prompt('Link URL');

      if (linkHref) {
        // Uses the Draft.js API to create a new entity with the right data.
        const contentWithEntity = content.createEntity(entityType.type, 'IMMUTABLE', {
          href: linkHref,
        });
        const entityKey = contentWithEntity.getLastCreatedEntityKey();

        // We also add some text for the entity to be activated on.
        const text = `${linkText}`;

        const newContent = Modifier.replaceText(content, selection, text, null, entityKey);
        const nextState = EditorState.push(editorState, newContent, 'insert-characters');

        onComplete(nextState);
      } else {
        onComplete(editorState);
      }
    } else {
      onComplete(editorState);
    }
  }

  render() {
    return null;
  }
}

const NonModalLink = (props) => {
  const { entityKey, contentState } = props;
  const data = contentState.getEntity(entityKey).getData();

  return React.createElement(
    'a',
    {
      role: 'button',
      onClick: () => {window.alert(data.href)}
    },
    props.children,
  );
};

window.draftail.registerPlugin({
  type: 'NONMODALLINK',
  source: NonModalLinkSource,
  decorator: NonModalLink,
});
