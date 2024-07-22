from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

class Car(models.Model):
    brand = models.CharField(max_length=100, blank=False, null=False)
    model = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField()
    is_bought = models.BooleanField(default=True, blank=False, null=False)
    buy_time = models.DateTimeField(default=timezone.now)
    buyer_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model} has bought by {self.buyer_id} for {self.price}$"

    def get_absolute_url(self):
        return reverse("cars_app:car_details", kwargs={"pk": self.pk})