# Generated by Django 4.2.7 on 2023-11-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CDR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('called_number', models.CharField(max_length=15)),
                ('calling_number', models.CharField(max_length=15)),
                ('call_start_time', models.DateTimeField()),
                ('call_end_item', models.DateTimeField()),
                ('call_duration', models.IntegerField()),
                ('status', models.CharField(choices=[('s', 'Успешный'), ('r', 'Отклоненный'), ('m', 'Пропущенный')], default='s', max_length=1)),
                ('call_type', models.CharField(choices=[('o', 'Исходящий'), ('i', 'Входящий'), ('m', 'Пропущенный')], max_length=1)),
            ],
        ),
    ]
