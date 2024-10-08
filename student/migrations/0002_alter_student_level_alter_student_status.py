# Generated by Django 5.1.1 on 2024-09-09 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.level', verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('Учится', 'Учится'), ('В академ. отпуске', 'В академ. отпуске'), ('Возврат', 'Возврат'), ('Закончил обучение', 'Закончил обучение')], max_length=100, verbose_name='Статус'),
        ),
    ]
