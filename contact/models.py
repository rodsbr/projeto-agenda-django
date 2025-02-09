from django.db import models
from django.utils import timezone

#id(primary key)
# Create your models here.
# first_name(string), last_name(string), phone(string)
# email(email), created_date(date), description(text)

# Depois
# category(foreing key), show (boolean), owner (forein key)
# picture (image)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
