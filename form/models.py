from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.FileField(upload_to='books/',blank=True,null=True)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title