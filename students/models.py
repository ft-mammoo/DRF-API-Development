from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name
