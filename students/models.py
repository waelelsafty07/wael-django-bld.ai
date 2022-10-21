from django.db import models


# Create your models here.


class Students(models.Model):  # table
    # integer, increments automatically
    id = models.AutoField(primary_key=True)
    # column varchar = CharField()
    firstname = models.CharField(max_length=200)
    # can't be empty nor null - may be not applicable for sqlite
    lastname = models.TextField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'students'
