# Generated by Django 3.2.8 on 2021-11-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdata',
            name='rating',
            field=models.CharField(default=4, max_length=5),
        ),
    ]
