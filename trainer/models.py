from django.db import models
from django.shortcuts import redirect


class Trainer(models.Model):
    department_options = (
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('network', 'Network')
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    department = models.CharField(choices=department_options, max_length=8)
    active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def delete(self, *args, **kwargs):
        self.active = False
        return super().save(*args, **kwargs)