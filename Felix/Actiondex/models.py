from django.db import models

# Create your models here.
class Drug(models.Model):
    drug_id = models.IntegerField()
    name = models.CharField(max_length=200)

class Subject(models.Model):
    subject_id = models.IntegerField()
    disease = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)

class Trial(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    time = models.DateField('trial date')
