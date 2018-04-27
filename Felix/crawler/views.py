from django.shortcuts import render

from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def index(request):
    return render(request, 'index.html')

def capture(url, label, attr, pool):
    '''
    capture new urls located at **attributes** of **labels** from **source urls**, 
    grow **pool of target urls** and return it.
    '''
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

def search(depth, imgs, targets, visited):
    try:
        togo = targets.pop()
    except KeyError:
        return imgs
    imgs = capture(togo, 'img', 'src', imgs)
    visited.add(togo)
    if depth==1:
        return imgs
    else:
        targets = capture(togo, 'a', 'href', targets)
        return search(depth-1, imgs, targets, visited)
    

def crawl(request):
    imgs = set(search(int(request.POST['depth']), [], [request.POST['start']], set()))   
    context = {
        'imgs':imgs,
    }
    return render(request, 'result.html', context)
