// TODO: find proper types for ace
declare const ace: any; // eslint-disable-line @typescript-eslint/no-explicit-any

// import 'ace/webpack-resolver';

import { css_beautify, html_beautify, js_beautify } from 'js-beautify';

const initAceEditor = (widgetID: string): void => {
  if (widgetID) {
    const editorNode = document.getElementById(`${widgetID}-ace-editor`);
    const inputNode = document.getElementById(widgetID) as HTMLInputElement;

    const getBeautifiedValue = (mode?: string, value = '') => {
      if (mode === 'html') {
        return html_beautify(value);
      }

      if (mode === 'javascript') {
        return js_beautify(value);
      }

      if (mode === 'css') {
        return css_beautify(value);
      }

      return value;
    };

    if (editorNode && inputNode) {
      try {
        const mode = editorNode.dataset.mode;
        ace.config.set('basePath', 'https://cdnjs.cloudflare.com/ajax/libs/ace/1.11.2/');
        // ace.config.setModuleUrl('ace/mode/html', 'https://cdnjs.cloudflare.com/ajax/libs/ace/1.11.2/mode-html.js');

        const editor = ace.edit(editorNode);
        editor.setTheme('ace/theme/monokai'); //TODO: set theme dynamically
        editor.session.setMode(`ace/mode/${mode}`);
        editor.session.setValue(getBeautifiedValue(mode, editor.session.getValue()));
        // console.log(mode, beautify);

        // const beautify = ace.require('ace/ext/beautify');
        // console.log(beautify);

        editor.getSession().on('change', () => {
          console.log('testing');

          inputNode.value = getBeautifiedValue(mode, editor.getSession().getValue());
        });
      } catch (error) {
        editorNode.innerHTML = `Rendering Error: ${(error as any).message}`;
      }
    }
  }
};

export { initAceEditor as init };
