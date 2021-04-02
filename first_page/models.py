from django.db import models

class User(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    add = models.CharField(max_length = 20)
    marks = models.IntegerField()


class contact(models.Model):
    mobile = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
