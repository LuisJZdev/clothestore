# Django
from django.db import models
from django.contrib.auth.models import User

# My apps
from clothes.models import PledgeColorSet

class Cart(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    products = models.ManyToManyField(to=PledgeColorSet)

    def __str__(self) -> str:
        return f"user '{self.user.username}' cart"

    def total_price(self) -> int:
        total_price = 0

        for set in self.products.all():
            total_price += set.price
        
        return total_price