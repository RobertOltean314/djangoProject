# Generated by Django 4.2.7 on 2023-11-18 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='resume',
            new_name='description',
        ),
    ]
