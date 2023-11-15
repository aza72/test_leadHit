from django.db import models

class TempForms(models.Model):
    name_temp = models.ForeignKey('NameTemp', on_delete=models.CASCADE, max_length=255, verbose_name='Имя формы')
    name_field = models.CharField(max_length=255,verbose_name='Имя поля')
    name_type = models.CharField(max_length=255,verbose_name='Тип данных поля')

    def __str__(self):
        return self.name_field

class NameTemp(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name
