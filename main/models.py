from django.db import models

# Create your models here.
class Record(models.Model):
    data = models.TextField('data')
    pub_date = models.DateTimeField('date published')

