# Generated by Django 3.2.8 on 2021-11-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('productName', models.CharField(max_length=100)),
            ],
        ),
    ]
