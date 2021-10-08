from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return f'{self.name}\'s email is {self.email} and the phone number is {self.phone_number}.'
