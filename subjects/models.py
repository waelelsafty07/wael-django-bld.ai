from django.db import models


class Subjects(models.Model):  # table
    # column varchar = CharField()
    name = models.CharField(max_length=200) 

    class Meta:
        db_table = 'subjects'
