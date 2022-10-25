from django.db import models

# Create your models here.


class Subjects(models.Model):  # table
    # integer, increments automatically
    id = models.AutoField(primary_key=True)
    # column varchar = CharField()
    name = models.CharField(max_length=200)
    # can't be empty nor null - may be not applicable for sqlite

    class Meta:
        db_table = 'subjects'
