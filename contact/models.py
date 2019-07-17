from django.db import models

# Create your models here.

class data(models.Model):
    name = models.CharField(max_length=64)
    company = models.CharField(max_length=100)
    field = models.CharField(max_length=64)
    budget = models.SmallIntegerField()
    phone = models.BigIntegerField()
    requirements = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name[:15]