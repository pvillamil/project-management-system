from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator


status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=80)
    assign = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    efforts = models.DurationField(null=True)
    status = models.CharField(max_length=7, choices=status, default=1)
    dead_line = models.DateField()
    company = models.ForeignKey('register.Company', on_delete=models.DO_NOTHING, null=True)
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])

    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return (self.name)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, null=True)
    task_name = models.CharField(max_length=80)
    status = models.CharField(max_length=7, choices=status, default=1)
    due = models.CharField(max_length=7, choices=due, default=1, null=True)

    def __str__(self):
        return(self.task_name)