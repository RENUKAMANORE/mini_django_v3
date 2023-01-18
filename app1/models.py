from django.db import models

class MyModel(models.Model):
    field = models.CharField(max_length=250)
    field2 = models.CharField(max_length=250)

