from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=100)
    today_price = models.DecimalField(max_digits=10, decimal_places=2)
    predicted_price = models.DecimalField(max_digits=10, decimal_places=2)
    mse = models.DecimalField(max_digits=10, decimal_places=2)
