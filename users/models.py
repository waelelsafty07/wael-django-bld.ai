from django.db import models
from parents.models import Parents

# Create your models here.


class Users(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, unique=True)
    parent = models.OneToOneField(
        Parents, related_name="parentAccount", on_delete=models.CASCADE)

    def __str__(self):
        return self.parent

    class Meta:
        indexes = [models.Index(
            fields=['email'], name='email_index')]
        db_table = 'users'


class Tokens(models.Model):  # table
    # column varchar = CharField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(
        Parents, related_name='parent', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tokens'
