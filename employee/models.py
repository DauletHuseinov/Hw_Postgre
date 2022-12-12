from django.db import models
from datetime import date


# Create your models here.
from django.db import models


# Create your views here.

class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField(default='1990-01-01')

    class Meta:
        abstract = True


class Employee(AbstractPerson):
    position = models.CharField(max_length=20)
    salary = models.IntegerField()
    work_experience = models.IntegerField()

    def __str__(self):
        return f'{self.name}-{self.birth_date}'


class Passport(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    inn = models.CharField(max_length=14)
    id_card = models.IntegerField()

    def get_gender(self):
        for inn in self.inn:
            if inn[0] == '1':
                return 'Female'
            else:
                return 'Male'


class WorkProject(models.Model):
    employee = models.ManyToManyField(Employee, through='Membership')
    project_name = models.CharField(max_length=60)

    def __str__(self):
        return self.project_name


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def save(self, *args, **kwargs):
        print(f'Было сохранено: '
              f'Имя сотрудника: {self.employee.name}'
              f'Дата рождения: {self.employee.birth_date}'
              f'Зароботная плата: {self.employee.salary}'
              f'Опыт работы: {self.employee.work_experience}'
              f'Название проекта: {self.work_project.project_name}'
              f'Дата присоединения: {self.date_joined}')
        super().save(*args, **kwargs)


class Client(AbstractPerson):
    address = models.CharField(max_length=35)
    phone_number = models.IntegerField()


class VIPClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()
