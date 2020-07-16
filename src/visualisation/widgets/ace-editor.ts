import * as _Plotly from 'plotly.js';
// TODO: find proper types for ace
declare const ace: any; // eslint-disable-line @typescript-eslint/no-explicit-any
declare const Plotly: typeof _Plotly;

const renderChart = (options: string, element: HTMLElement) => {
  element.innerHTML = '';
  const { data, layout } = JSON.parse(options);

  return Plotly.newPlot(element, data, layout);
};

const initPlotlyPreview = (widgetID: string, options: string) => {
  const previewNode = document.getElementById(`${widgetID}-plotly-preview`);
  if (previewNode) {
    try {
      renderChart(options, previewNode);

      return {
        onUpdate: (options: string) => {
          try {
            renderChart(options, previewNode);
          } catch (error) {
            previewNode.innerHTML = `Rendering Error: ${error.message}`;
          }
        },
      };
    } catch (error) {
      previewNode.innerHTML = `Rendering Error: ${error.message}`;
    }
  }

  return null;
};

const initAceEditor = (widgetID: string): void => {
  if (widgetID) {
    const editorNode = document.getElementById(`${widgetID}-ace-editor`);
    const inputNode = document.getElementById(widgetID) as HTMLInputElement;
    if (editorNode && inputNode) {
      try {
        const editor = ace.edit(editorNode);
        editor.setTheme('ace/theme/monokai'); //TODO: set theme dynamically
        editor.session.setMode('ace/mode/json'); //TODO: set mode dynamically

        let preview = initPlotlyPreview(widgetID, inputNode.value);

        editor.getSession().on('change', () => {
          inputNode.value = editor.getSession().getValue();
          if (preview) {
            preview.onUpdate(inputNode.value);
          } else {
            preview = initPlotlyPreview(widgetID, inputNode.value);
          }
        });
      } catch (error) {
        editorNode.innerHTML = `Rendering Error: ${error.message}`;
      }
    }
  }
};

export { initAceEditor as init };
