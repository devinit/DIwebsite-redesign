from django.shortcuts import render
from django.http import HttpResponse


def error_404_view(request, exception):
    data = {"status": 404}
    return render(request,'404-static.html', data)