import * as _Plotly from 'plotly.js';
declare const ace: any; // TODO: find proper types
declare const Plotly: typeof _Plotly;

const renderChart = (options: string, element: HTMLElement) => {
    const { data, layout } = JSON.parse(options);

    return Plotly.newPlot(element, data, layout);
}

const initPlotlyPreview = (widgetID: string, options: string) => {
    const previewNode = document.getElementById(`${widgetID}-plotly-preview`);
    if (previewNode) {
        try {
            renderChart(options, previewNode);

            return {
                onUpdate: (options: string) => {
                    renderChart(options, previewNode);
                }
            }
        } catch (error) {
            console.log(error);
        }
    }

    return null;
}

const initAceEditor = (widgetID: string) => {
    if (widgetID) {
        const editorNode = document.getElementById(`${widgetID}-ace-editor`);
        const inputNode = document.getElementById(widgetID) as HTMLInputElement;
        if (editorNode && inputNode) {
            const editor = ace.edit(editorNode);
            editor.setTheme("ace/theme/monokai"); //TODO: set theme dynamically
            editor.session.setMode("ace/mode/json"); //TODO: set mode dynamically

            const preview = initPlotlyPreview(widgetID, inputNode.value);

            editor.getSession().on('change', () => {
                inputNode.value = editor.getSession().getValue();
                if (preview) {
                    preview.onUpdate(inputNode.value);
                }
            });
        }
    }
}

export { initAceEditor as init };
