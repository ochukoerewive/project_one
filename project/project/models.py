from django.db import models
class DetailsModel(models.Model):
    id=models.AutoFields(primary_key=True)
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    def __str__ (self):
        return self.name