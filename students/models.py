from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cgpa = models.FloatField()
    skills = models.TextField(blank=True)
    

    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    min_cgpa = models.FloatField()
    required_skills = models.CharField(max_length=200)

    def __str__(self):
        return self.name