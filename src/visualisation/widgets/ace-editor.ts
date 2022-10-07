// TODO: find proper types for ace
declare const ace: any; // eslint-disable-line @typescript-eslint/no-explicit-any

// import 'ace/webpack-resolver';

const initAceEditor = (widgetID: string): void => {
  if (widgetID) {
    const editorNode = document.getElementById(`${widgetID}-ace-editor`);
    const inputNode = document.getElementById(widgetID) as HTMLInputElement;
    if (editorNode && inputNode) {
      try {
        const mode = editorNode.dataset.mode;
        ace.config.set('basePath', 'https://cdnjs.cloudflare.com/ajax/libs/ace/1.11.2/');
        // ace.config.setModuleUrl('ace/mode/html', 'https://cdnjs.cloudflare.com/ajax/libs/ace/1.11.2/mode-html.js');

        const editor = ace.edit(editorNode);
        editor.setTheme('ace/theme/monokai'); //TODO: set theme dynamically
        editor.session.setMode(`ace/mode/${mode}`);

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
