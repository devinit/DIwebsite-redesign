from django.urls import path

from di_website.api.views import footer_view, spotlights_navigation_view, spotlight_pages_view

urlpatterns = [
    path('spotlights/navigation/', spotlights_navigation_view, name='spotlight-navigation'),
    path('spotlights/pages/', spotlight_pages_view, name='spotlight-pages'),
    path('footer/', footer_view)
]
