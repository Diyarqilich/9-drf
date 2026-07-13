from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    surename = models.CharField(max_length=100,blank=False, null=False)
    age = models.PositiveIntegerField(null=False,blank=True,default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name