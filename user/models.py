from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField('user_name',max_length=50)
    email = models.EmailField('email',unique=True)
    password = models.CharField('password',max_length=500)


    @staticmethod
    def dummy_user():
        return User(id='',userName='',email='',password='')


    class Meta:
        db_table='User'
