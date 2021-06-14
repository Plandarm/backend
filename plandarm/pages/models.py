from django.db import models
from accounts.models import Profile
# Create your models here.

class Page(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True) 
    html = models.TextField(null=True)

    create_date = models.DateTimeField(auto_now_add=True, null=True)
    change_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title