from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Doctor(models.Model):
    name = models.CharField()
    fullname = models.CharField()
    profession = models.CharField()
    age = models.IntegerField()
    work_experience = models.IntegerField()
    raiting = models.FloatField()

