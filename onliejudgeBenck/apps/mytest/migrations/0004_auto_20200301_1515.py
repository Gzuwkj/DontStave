# Generated by Django 2.2 on 2020-03-01 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0003_book_bn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auth',
            old_name='bk',
            new_name='book',
        ),
    ]
