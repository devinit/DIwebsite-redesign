from django.urls import path

from di_website.api.views import spotlights_navigation_view, footer_view

urlpatterns = [
    path('spotlights/navigation/', spotlights_navigation_view, name='spotlight-navigation'),
    path('footer/', footer_view)
]
