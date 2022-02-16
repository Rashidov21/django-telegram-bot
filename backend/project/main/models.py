from django.db import models

# Create your models here.
class Words(models.Model):

    GENDERS = [
        ('der', "Der"),
        ('die', "Die"),
        ('das', "Das"),
    ]
