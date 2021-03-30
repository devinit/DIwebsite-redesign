from django.urls import path

from di_website.api.views import (
    footer_view, spotlights_navigation_view, spotlight_page_view,
    spotlight_pages_view, dashboard_data_view)

urlpatterns = [
    path('spotlights/navigation/', spotlights_navigation_view, name='spotlight-navigation'),
    path('spotlights/pages/', spotlight_pages_view, name='spotlight-pages'),
    path('spotlights/page/<slug:slug>/', spotlight_page_view, name='spotlight-page'),
    path('footer/', footer_view),
    path('dashboard/data/', dashboard_data_view)
]
