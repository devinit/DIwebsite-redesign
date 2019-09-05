from django.shortcuts import render
from django.http import HttpResponse


def error_404_view(request, exception):
    data = {"status": 404}
    return render(request,'404.html', data)

def error_500_view(request):
    data = {"status": 500}
    return render(request,'500.html', data)