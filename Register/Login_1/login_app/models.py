from django.db import models

class Register_Model(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    contact=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username
