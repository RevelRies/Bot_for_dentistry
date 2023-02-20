# Generated by Django 4.1.6 on 2023-02-19 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Профиль',
            },
        ),
        migrations.AlterField(
            model_name='doctor',
            name='fullname',
            field=models.CharField(max_length=128, verbose_name='Полное имя доктора'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Сокращенное имя доктора для вывода в меню'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profession',
            field=models.CharField(max_length=128, verbose_name='Профессия'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='raiting',
            field=models.FloatField(verbose_name='Оценка доктора'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='work_experience',
            field=models.IntegerField(verbose_name='Опыт работы'),
        ),
    ]
