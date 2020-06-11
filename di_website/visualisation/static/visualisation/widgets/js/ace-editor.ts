declare const ace: any; // TODO: find proper types

const initAceEditor = (widgetID: string) => {
    if (widgetID) {
        const editorNode = document.getElementById(`${widgetID}-ace-editor`);
        const inputNode = document.getElementById(widgetID) as HTMLInputElement;
        if (editorNode && inputNode) {
            const editor = ace.edit(editorNode);
            editor.setTheme("ace/theme/monokai"); //TODO: set theme dynamically
            editor.session.setMode("ace/mode/json"); //TODO: set mode dynamically
            editor.getSession().on('change', () => {
                inputNode.value = editor.getSession().getValue();
            });
        }
    }
}
