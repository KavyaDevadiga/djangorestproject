from django.db import models

# Create your models here.
class Bookstore(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    vol=models.IntegerField()
    copies=models.IntegerField()
    store=models.CharField(max_length=100)
    gid=models.CharField(null=True,max_length=100)
    owner=models.ForeignKey('auth.User',related_name="books",on_delete=models.CASCADE,null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)