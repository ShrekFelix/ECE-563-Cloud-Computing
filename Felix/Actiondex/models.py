from django.db import models

# Create your models here.
class Drug(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    def __str__(self):
        return str((self.name))

class Subject(models.Model):
    disease = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    def __str__(self):
        return str((self.disease, self.occupation))

class Trial(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    result = models.CharField(max_length=200)
    lesson = models.CharField(max_length=200)
    time = models.DateField('trial date')
    def __str__(self):
        return str((self.drug, self.subject, self.result, self.lesson, self.time))
