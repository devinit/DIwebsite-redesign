export const FOOTNOTE_CHOOSER_MODAL_ONLOAD_HANDLERS = {
    'chooser': function(modal, jsonData) {
        $('form.footnote-form', modal.body).on('submit', function() {
            var formdata = new FormData(this);

            $.ajax({
                url: this.action,
                data: formdata,
                processData: false,
                contentType: false,
                type: 'POST',
                dataType: 'text',
                success: modal.loadResponseText
            });

            return false;
        });
    },
    'footnote_chosen': function(modal, jsonData) {
        modal.respond('footnoteChosen', jsonData['footnote_data']);
        modal.close();
    }
};
