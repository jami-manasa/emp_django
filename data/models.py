from django.db import models


# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Assets(models.Model):
    assets=models.CharField(max_length=100)

    def __str__(self):
        return self.assets

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)
    # assets=models.ForeignKey(Assets,on_delete=models.CASCADE)
    # iteams=models.CharField(max_length=100)
class table(models.Model):
    emp=models.ForeignKey(Employee,on_delete=models.CASCADE)
    lst=models.CharField(max_length=250)

