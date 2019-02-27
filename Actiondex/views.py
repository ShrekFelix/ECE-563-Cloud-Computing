from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Trial, Drug, Subject

import datetime

def index(request):
    return render(request, 'index.html')

def query(request):
    drug_name = request.POST['drug_name']
    subject_occupation = request.POST['subject_occupation']
    subject_disease = request.POST['subject_disease']

    drug = Drug.objects.filter(name = drug_name).values('name')
    subject = Subject.objects.filter( Q(occupation = subject_occupation) | Q(disease = subject_disease) ).values('id')
    result = Trial.objects.filter( Q(drug__in = drug) | Q(subject__in = subject) )
    print(result)
    context = {
        'result':result
    }
    return render(request, 'result.html', context)

def insert(request):
    drug_name = request.POST['drug_name']
    subject_occupation = request.POST['subject_occupation']
    subject_disease = request.POST['subject_disease']
    result = request.POST['result']
    lesson = request.POST['lesson']
    drug = Drug(name = drug_name)
    drug.save()
    subject = Subject(disease = subject_disease, occupation = subject_occupation)
    subject.save()
    trial = Trial(drug = drug, subject = subject, result = result, lesson = lesson, time = datetime.date.today())
    trial.save()