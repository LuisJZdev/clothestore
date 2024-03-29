# Django
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

# My apps
from clothes.models import PledgeColorSet, Size

class Cart(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    products = models.ManyToManyField(to=PledgeColorSet, through="CartPledge")

    def __str__(self) -> str:
        return f"user '{self.user.username}' cart"

    def total_price(self) -> int:
        total_price = 0

        for set in self.products.all():
            total_price += set.price
        
        return total_price
    
    def succesful_purchase(self):
        """
        Create SuccesfulPurchase models for each product in cart
        """

        for pledge in self.cartpledge_set.all():
            pledge.pledgecolorset.succesfulpurchase_set.create(date=timezone.now().date())

class CartPledge(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    pledgecolorset = models.ForeignKey(to=PledgeColorSet, on_delete=models.CASCADE)

    size = models.ForeignKey(to=Size, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.cart.__str__()} with {self.pledgecolorset.__str__()} with the size {self.size.name}"
    
    def save(self, *args, **kwargs) -> None:

        # It can't be added the same product more than one time
        try:
            CartPledge.objects.get(cart=self.cart, pledgecolorset=self.pledgecolorset, size=self.size)
            raise ValueError("object already in this cart")
        except ObjectDoesNotExist:
            return super().save(*args, **kwargs)
        
class SuccesfulPurchase(models.Model):
    pledgecolorset = models.ForeignKey(to=PledgeColorSet, on_delete=models.CASCADE)

    date = models.DateField(default=timezone.now().date())

    def __str__(self) -> str:
        return f"{self.pledgecolorset.pledge.name} sold in {self.date}" 