from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    min_cgpa = models.FloatField()
    required_skills = models.CharField(max_length=200)

    def __str__(self):
        return self.name