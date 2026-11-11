from django.db import models
from datetime import datetime
# class Project(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    

class Department(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

class Project(models.Model):
    title=models.CharField(max_length=200)
    student_name=models.CharField(max_length=150)
    registration_number=models.CharField(max_length=30)
    description=models.TextField()
    date_submitted=models.DateTimeField(default=datetime.now)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name=("department"),
    )
