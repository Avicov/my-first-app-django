from django.db import models
from django.utils import timezone

class Autor(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()

class Post(models.Model):
    author = models.ForeignKey(Autor)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



# Create your models here.
