# Generated by Django 2.2 on 2020-03-01 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0002_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bn',
            field=models.CharField(default='', max_length=100),
        ),
    ]
