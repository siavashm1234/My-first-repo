from django.db import models


class Animal (models.Model):
    Animal_Species = models.CharField(max_length=200)
    Animal_Name = models.CharField(max_length=200)
    animal_Age = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Animal_Name} ({self.Animal_Species})"