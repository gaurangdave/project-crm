from django.db import models

# Create your models here.

# This is a model for the Greetings table, a simple hello world message


class Greetings(models.Model):
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
