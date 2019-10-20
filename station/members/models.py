from django.db import models

# Create your models here.

TOUR = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)

PLATOON = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
)


class LT(models.Model):
    Last_Name = models.CharField(max_length=25)
    First_Name = models.CharField(max_length=25)
    Shield = models.IntegerField()
    Tour = models.CharField(max_length=1, choices=TOUR)
    Platoon = models.CharField(max_length=1, choices=PLATOON)
    TED = models.DateField()
    ODA = models.DateField()

    def __str__(self):
        return self.Last_Name + ', ' + self.First_Name


class MEDIC(models.Model):
    Last_Name = models.CharField(max_length=25)
    First_Name = models.CharField(max_length=25)
    Shield = models.IntegerField()
    Tour = models.CharField(max_length=1, choices=TOUR)
    Platoon = models.CharField(max_length=1, choices=PLATOON)
    Unit = models.CharField(max_length=4)
    TED = models.DateField()
    ODA = models.DateField()

    def __str__(self):
        return self.Last_Name + ', ' + self.First_Name

class EMT(models.Model):
    Last_Name = models.CharField(max_length=25)
    First_Name = models.CharField(max_length=25)
    Shield = models.IntegerField()
    Tour = models.CharField(max_length=1, choices=TOUR)
    Platoon = models.CharField(max_length=1, choices=PLATOON)
    Unit = models.CharField(max_length=4)
    ODA = models.DateField()

    def __str__(self):
        return self.Last_Name + ', ' + self.First_Name