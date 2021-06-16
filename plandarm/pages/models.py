from django.db import models
from accounts.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


class Page(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, default="New Page") 
    html = models.TextField(default='<p class="block text-block"></p>')
    viewers = models.ManyToManyField(Profile, related_name='viewable_pages')

    create_date = models.DateTimeField(auto_now_add=True, null=True)
    change_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.owner}:{self.id}:{self.title}"


@receiver(post_save, sender=Profile)
def create_default_page(sender, instance, created, **kwargs):
    if created:
        Page.objects.create(owner=instance)
