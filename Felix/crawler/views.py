from django.shortcuts import render

from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup


def index(request):
    return render(request, 'index.html')

def crawl(request):
    ext = '.png'
    url = request.POST['input']
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    results = []
    for node in soup.find_all('img'):
        src = node.get('src')
        if src:
            if src.endswith(ext):
                if src.startswith('/'):#relative path
                    src = url+src
                results.append(src)
    context = {
        'results':results,
    }
    return render(request, 'result.html', context)
