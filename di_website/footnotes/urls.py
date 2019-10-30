from django.conf.urls import url
from di_website.footnotes.views import chooser

app_name = 'footnotes'
urlpatterns = [
    url(r'^chooser/$', chooser.chooser, name='chooser'),
    url(r'^chooser/upload/$', chooser.chooser_upload, name='chooser_upload'),
]
