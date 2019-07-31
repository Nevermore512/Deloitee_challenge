from django.db import models

class sheet(models.Model):
    name = models.CharField(max_length=120)
    balance_sheet = models.FileField(upload_to='balance')
    income = models.FileField(upload_to='income')
    cash_flow = models.FileField(upload_to='carsh')

