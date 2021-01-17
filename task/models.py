from django.db import models

# Create your models here.

from categorie.models import Categories

class Task(models.Model):
    taskTitle = models.CharField('task_title',max_length=50)
    description = models.CharField('description',max_length=500)
    cateref = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='taskref',null=True)


    @staticmethod
    def dummy_task():
        return Task(id='',taskTitle ='',description='', cateref='')


    class Meta:
        db_table='Task'
