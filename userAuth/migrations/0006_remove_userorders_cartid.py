# Generated by Django 3.2.8 on 2021-11-10 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0005_auto_20211109_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorders',
            name='cartId',
        ),
    ]
