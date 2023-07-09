from django.db import models


class School(models.Model):
    name = "about us"
    about_us = models.TextField(verbose_name="About Us")
    address = models.TextField(verbose_name="Address")

    class Meta:
        verbose_name_plural = "School"

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=250)
    registration_number = models.IntegerField(default=None)
    class_number = models.IntegerField(null=False)
    roll_number = models.IntegerField(default=None)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
