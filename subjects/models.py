from django.db import models


class Subjects(models.Model):  # table
    # column varchar = CharField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subjects'
