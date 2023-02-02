from django.db import models
from django.conf import settings
from company.models import food


class reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    no_of_people = models.PositiveIntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    food = models.ForeignKey(food, on_delete=models.CASCADE)


class favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    food = models.ForeignKey(food, on_delete=models.CASCADE)


class feedback(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    reservation = models.ForeignKey(
        reservation, null=True, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=122)
    feedback = models.CharField(max_length=122)

    def __str__(self):
        return self.title
