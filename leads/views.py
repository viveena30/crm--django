from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # return HttpResponse("Home page ")
    # return render(request, 'leads/home_page.html')
    return render(request, 'second_page.html')

