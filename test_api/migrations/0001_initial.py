# Generated by Django 4.2.7 on 2023-11-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TempForms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_temp', models.CharField(max_length=255)),
                ('name_field', models.CharField(max_length=255)),
                ('name_type', models.CharField(max_length=255)),
            ],
        ),
    ]
