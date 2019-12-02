
def serialise_page(page, request):
    return {
        'title': page.title,
        'full_url': page.full_url,
        'relative_url': page.relative_url(request.site, request),
        'active': page.active
    }
