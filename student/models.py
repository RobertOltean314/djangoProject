from django.db import models

from trainer.models import Trainer


class Student(models.Model):
    gender_options = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    gender = models.CharField(choices=gender_options, max_length=6)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True)

    # auto_now_add=True, folosit pentru a va stoca data si ora in momentul in care este salvat studentul. Nu se mai modifica data si ora
    # auto_now=True, folosit pentru a stoca data si ora de fiecare data cand se modifica date pe respecitva inregistrare

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
