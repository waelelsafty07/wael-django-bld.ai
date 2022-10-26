from django.db import models

from parents.models import Parents
from subjects.models import Subjects

# Create your models here.


class Students(models.Model):  # table
    firstname = models.CharField(max_length=200)
    # can't be empty nor null - may be not applicable for sqlite
    lastname = models.TextField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=255, unique=True)

    mark = models.IntegerField()
    parent = models.ForeignKey(
        Parents, related_name='parents', on_delete=models.CASCADE)
    subjects = models.ManyToManyField(
        Subjects, related_name='parents')

    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        db_table = 'students'
        ordering = ['age']  # default ordering without order_by

        indexes = [models.Index(
            fields=['firstname'], name='first_name_index')]
        # index on multiple columns
        indexes = [models.Index(
            fields=['firstname', 'lastname'], name='first_last_name_index')]

        constraints = [
            models.CheckConstraint(
                name='age greater than 5', check=models.Q(age__gt=5))
        ]
