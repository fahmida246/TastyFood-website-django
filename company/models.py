from django.db import models

# Create your models here.
# from customer.models import reservation
from django.conf import settings


class food(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=122)
    type = models.CharField(max_length=122)
    describtion = models.TextField()
    price = models.CharField(max_length=122)
    image = models.ImageField(upload_to='profileimg', blank=True)

    def __str__(self):
        return self.name


class blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=122)
    describtion = models.TextField()
    image = models.ImageField(upload_to='profileimg', blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



