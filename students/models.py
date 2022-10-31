from django.db import models
from django.core.validators import RegexValidator


# from users.models import User
from parents.models import Parents
from subjects.models import Subjects

# Create your models here.

validate_name = RegexValidator(
    regex='^[A-Z][a-zA-Z ]*$', message='Name must start with a capital letter and contain only letters')


class Students(models.Model):  # table
    firstname = models.CharField(max_length=200, validators=[validate_name])
    # can't be empty nor null - may be not applicable for sqlite
    lastname = models.TextField(max_length=200, validators=[validate_name])
    age = models.IntegerField()

    mark = models.IntegerField()
    parent = models.ForeignKey(
        Parents, related_name='childern', on_delete=models.CASCADE)
    subjects = models.ManyToManyField(
        Subjects, related_name='subjects')

    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        db_table = 'students'
        # ordering = ['age']  # default ordering without order_by

        indexes = [models.Index(
            fields=['firstname'], name='first_name_index')]
        # index on multiple columns
        indexes = [models.Index(
            fields=['firstname', 'lastname'], name='first_last_name_index')]
