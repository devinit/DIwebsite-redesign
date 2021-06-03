import $ from 'jquery';

export default function listShowHide (
        selector='[data-js="toggleable-list"]',
        item='[data-js="toggleable-list--item"]',
    ) {

    const lists = $(selector);

    if (!lists.length) {
        return;
    }

    lists.each((index, element) =>{

        const list = $(element);
        const items = list.find(item);

        if (!items.length) {
            return;
        }

        const button_class = list.data('button-class') || 'button';
        const show_text = list.data('show-text');
        const less_text = list.data('less-text');
        const comma_separated = list.data('comma-separated');
        let trigger = undefined;
        let is_visible = false;

        trigger = $(`<button class="${button_class}" type="button"><div style="display: inline;"></div><i class="icon"></i></button>`);

        toggleAll();
        trigger.insertAfter(list.first());

        // add handler to trigger
        $(trigger).on('click keypress', function(e) {
            e.preventDefault();
            if (isValidAction(e)) {
                is_visible = !is_visible;
                toggleAll();
            }
        });

        // toggle all items
        function toggleAll() {
            toggleComma();
            toggleItemDisplay();
            toggleTriggerLabel();
            toggleAriaVal();
        }

        // toggle the last comma when active
        function toggleComma() {
            if (comma_separated) {
                try {
                    const last_child = list.children().not(item).last();
                    const contents = last_child.contents();

                    if (contents && contents.get(contents.length-1).nodeType == Node.TEXT_NODE) {
                        const text = contents.get(contents.length-1);
                        const text_content = text.textContent;
                        if (!is_visible) {
                            if (text_content.slice(-1) == ',') {
                                text.textContent = text_content.slice(0, -1) + ' ...';
                            }
                        }
                        else {
                            if (text_content.slice(-4) == ' ...') {
                               text.textContent = text_content.slice(0, -4) + ',';
                            }
                        }
                    }
                } catch (error) {}
            }
        }

        // toggle the item display
        function toggleItemDisplay() {
            items.toggle(is_visible);
        }

        // toggle the trigger label
        function toggleTriggerLabel() {
            trigger.find('div').text(is_visible ? less_text : show_text);
        }

        // toggle the aria val
        function toggleAriaVal() {
            items.attr('aria-hidden', !is_visible);
        }

    });

    // test for valid click or enter key press
    function isValidAction(e) {
        return e.key === 'Enter' || e.type === 'click';
    }
}
