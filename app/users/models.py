from django.db import models

# Create your models here.
from django.db import models


class Candidate(models.Model):
    """
    Candidate Model
    Defines the attributes of a Candidate
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_fullname(self):
        return f"Fullname is {first_name} {last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name} added"
