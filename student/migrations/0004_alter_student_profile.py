# Generated by Django 4.2.7 on 2023-11-18 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]
