// TODO: find proper types for ace
declare const ace: any; // eslint-disable-line @typescript-eslint/no-explicit-any

const initAceEditor = (widgetID: string): void => {
  if (widgetID) {
    const editorNode = document.getElementById(`${widgetID}-ace-editor`);
    const inputNode = document.getElementById(widgetID) as HTMLInputElement;
    if (editorNode && inputNode) {
      try {
        const editor = ace.edit(editorNode);
        editor.setTheme('ace/theme/monokai'); //TODO: set theme dynamically
        editor.session.setMode('ace/mode/json'); //TODO: set mode dynamically

        editor.getSession().on('change', () => {
          inputNode.value = editor.getSession().getValue();
        });
      } catch (error) {
        editorNode.innerHTML = `Rendering Error: ${error.message}`;
      }
    }
  }
};

export { initAceEditor as init };
