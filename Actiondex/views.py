from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import Trial, Drug, Subject
from django.urls import reverse

import datetime

def index(request):
    return render(request, 'index.html')

def index_trial(request):
    return render(request, 'trial.html')

def query(request):
    def integize(s):
        if s:
            return int(s)
        else:
            return -100
    def nonnullize(s):
        if s:
            return s
        else:
            return 'NA'
    drug_name = nonnullize(request.POST['drug_name'])
    subject_occupation = nonnullize(request.POST['subject_occupation'])
    subject_disease = nonnullize(request.POST['subject_disease'])
    subject_age = integize(request.POST['subject_age'])
    location = nonnullize(request.POST['location'])
    duration = integize(request.POST['duration'])

    drug = Drug.objects.filter( Q(name=drug_name) ).values('name')
    subject = Subject.objects.filter( 
        Q(occupation = subject_occupation) | 
        Q(disease = subject_disease) | 
        (Q(age__gte=subject_age-3)&Q(age__lte=subject_age+3)) 
    ).values('id')
    trial = Trial.objects.filter( 
        Q(drug__in=drug) | 
        Q(subject__in=subject) | 
        Q(location=location) | 
        (Q(duration__gte=duration-3)&Q(duration__lte=duration+3))
    )
    context = {
        'trial':trial
    }
    return render(request, 'query_result.html', context)

def insert(request):
    drug_name = request.POST['drug_name']
    subject_occupation = request.POST['subject_occupation']
    subject_disease = request.POST['subject_disease']
    subject_age = request.POST['subject_age']
    location = request.POST['location']
    duration = request.POST['duration']
    result = request.POST['result']
    lesson = request.POST['lesson']
    drug = Drug(name = drug_name)
    drug.save()
    subject = Subject(disease = subject_disease, occupation = subject_occupation)
    if subject_age:
        subject.age = int(subject_age)
    subject.save()
    trial = Trial(drug = drug, subject = subject, location = location, result = result, lesson = lesson, time = datetime.date.today())
    if duration:
        trial.duration = int(duration)
    trial.save()
    return HttpResponseRedirect('/Actiondex/trial/')