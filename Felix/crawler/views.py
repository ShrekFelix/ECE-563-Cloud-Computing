from django.shortcuts import render

from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup


def index(request):
    return render(request, 'index.html')

def crawl(request):
    ext = 'png'
    url = request.POST['input']
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    try:
        result = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
        r = 'success'
    except:
        r = 'fail'
    context = {
        'result':result,
    }
    return render(request, 'result.html', context)
