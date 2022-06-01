from django.db import models

class QueryTest(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
