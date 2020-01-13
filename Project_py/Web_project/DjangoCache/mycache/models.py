from django.db import models


# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=128)
    s_age = models.IntegerField(max_length=10)
    s_sex = models.BooleanField(default=True)

    class Meta:
        db_table = "Student"
