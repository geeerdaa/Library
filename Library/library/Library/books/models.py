from django.db import models
import datetime
from django.utils.timezone import now




class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    author = models.CharField(max_length=100, null=False)
    publication_date = models.DateField(default=now())


    def __str__(self):
        return self.title


class Readers(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    middle_name =  models.CharField(max_length=50, null=False)
