# Generated by Django 2.2.7 on 2021-01-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=500, verbose_name='description'),
        ),
    ]