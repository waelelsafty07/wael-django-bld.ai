from django.db import models


# Create your models here.


class Parents(models.Model):  # table
    # column varchar = CharField()

    name = models.CharField(max_length=200)
    # can't be empty nor null - may be not applicable for sqlite
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parents'
