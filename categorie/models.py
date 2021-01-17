from django.db import models

# Create your models here.

from board.models import Board

class Categories(models.Model):
    cateName = models.CharField('cate_name',max_length=50)
    bordref = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='cateref',null=True)


    @staticmethod
    def dummy_categorie():
        return Categories(id='',cateName='',boardref='')


    class Meta:
        db_table='Categories'
