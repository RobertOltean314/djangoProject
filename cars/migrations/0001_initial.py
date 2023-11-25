# Generated by Django 4.2.7 on 2023-11-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('brand', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('color', models.CharField(max_length=15)),
                ('horse_power', models.IntegerField()),
            ],
        ),
    ]
