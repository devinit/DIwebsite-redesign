from wagtail.admin.modal_workflow import render_modal_workflow
from di_website.footnotes.forms import FootnoteForm


def chooser(request):
    form = FootnoteForm(initial=request.GET.dict())

    return render_modal_workflow(
        request, 'footnotes/chooser/chooser.html', None,
        {'form': form},
        json_data={'step': 'chooser'}
    )


def chooser_upload(request):
    if request.method == 'POST':
        form = FootnoteForm(request.POST, request.FILES)

        if form.is_valid():
            text = form.cleaned_data['text']
            uuid = form.cleaned_data['uuid']
            footnote_data = {
                'text': text,
                'uuid': uuid,
            }
            return render_modal_workflow(
                request, None, None,
                None, json_data={'step': 'footnote_chosen', 'footnote_data': footnote_data}
            )
    else:
        form = FootnoteForm()

    return render_modal_workflow(
        request, 'footnotes/chooser/chooser.html', None,
        {'form': form},
        json_data={'step': 'chooser'}
    )
