# Generated by Django 4.2.7 on 2023-11-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_resume_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]
