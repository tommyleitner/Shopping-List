from django.db import models
from datetime import date


class ShoppingItem(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
