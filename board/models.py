from django.db import models

# Create your models here.

from user.models import User

class Board(models.Model):
    boardName = models.CharField('board_name',max_length=50)
    userref = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boardref',null=True)


    @staticmethod
    def dummy_board():
        return Board(id='',boardName='',userref='')


    class Meta:
        db_table='Board'
