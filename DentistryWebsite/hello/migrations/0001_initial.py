# Generated by Django 4.1.6 on 2023-02-25 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Сокращенное имя доктора для вывода в меню')),
                ('fullname', models.CharField(max_length=128, verbose_name='Полное имя доктора')),
                ('profession', models.CharField(max_length=128, verbose_name='Профессия')),
                ('age', models.IntegerField()),
                ('work_experience', models.IntegerField(verbose_name='Опыт работы')),
                ('raiting', models.FloatField(verbose_name='Оценка доктора')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время получения сообщения')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hello.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщенеия',
            },
        ),
    ]
