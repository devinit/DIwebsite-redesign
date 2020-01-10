from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^sitemap\.xml$', sitemap),
    url(r'^api/', include('di_website.api.urls')),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]

if settings.DEBUG:
    urlpatterns = [
        url(r'^robots\.txt$', TemplateView.as_view(template_name="includes/scaffold/robots.dev.txt", content_type='text/plain')),
    ] + urlpatterns
else:
    urlpatterns = [
        url(r'^robots\.txt$', TemplateView.as_view(template_name="includes/scaffold/robots.txt", content_type='text/plain')),
    ] + urlpatterns

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'test404', TemplateView.as_view(template_name='404.html')),
        url(r'test500', TemplateView.as_view(template_name='500.html')),
    ] + urlpatterns
    SHOW_TOOLBAR_CALLBACK = True
