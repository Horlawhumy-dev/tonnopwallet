# Generated by Django 4.0.5 on 2022-06-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('reg_number', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
