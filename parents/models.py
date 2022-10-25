from django.db import models

# Create your models here.


class Parents(models.Model):  # table
    # column varchar = CharField()
    firstname = models.CharField(max_length=200)
    # can't be empty nor null - may be not applicable for sqlite
    lastname = models.TextField(max_length=200)
    age = models.IntegerField()

    class Meta:
        db_table = 'parents'
