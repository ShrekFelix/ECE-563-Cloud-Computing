from django.shortcuts import render

from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def index(request):
    return render(request, 'index.html')

def crawl(request):
    
    start = request.POST['start']
    depth = int(request.POST['depth'])
    
    imgs=set()
    targets=set([start])
    visited=set()
    
    def capture(url, label, attr):
        '''
        capture new urls located at **attributes** of **labels** from **source urls**, 
        '''
        pool = []
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        url_obj = urlparse(url)
        for node in soup.find_all(label):
            new_url = node.get(attr)
            if new_url: # sometimes it's none
                if new_url.startswith(url_obj.path): # relative path
                    new_url = url_obj.scheme + '://' + url_obj.netloc + new_url
                if new_url.startswith(url_obj.scheme):
                    pool.append(new_url)
        return pool

    def search(depth):
        while len(targets)>0:
            togo = targets.pop()
            if togo in visited:
                break
            print(togo)
            imgs.update(capture(togo, 'img', 'src'))
            visited.add(togo)
        if depth!=1:
            targets.update(capture(togo, 'a', 'href'))
            return search(depth-1)
        else:
            return imgs

    context = {
        'imgs':search(depth),
    }
    return render(request, 'result.html', context)
