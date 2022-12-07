from django.http import HttpResponseRedirect


class NullInjectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        path = request.get_full_path()
        if ('%00' in path):
            new_path = path.replace('%00', '')
            return HttpResponseRedirect(new_path)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
