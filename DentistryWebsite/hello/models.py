from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Doctor(models.Model):
    name = models.CharField(max_length=128, verbose_name='Сокращенное имя доктора для вывода в меню')
    fullname = models.CharField(max_length=128, verbose_name='Полное имя доктора')
    profession = models.CharField(max_length=128, verbose_name='Профессия')
    age = models.IntegerField()
    work_experience = models.IntegerField(verbose_name='Опыт работы')
    raiting = models.FloatField(verbose_name='Оценка доктора')


class Profile(models.Model):
    external_id = models.PositiveIntegerField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"id: {self.external_id}, name: {self.name}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Message(models.Model):
    profile = models.ForeignKey(
        to='Profile',
        on_delete=models.PROTECT,
        verbose_name='Профиль'
    )

    text = models.TextField(verbose_name='текст')

    created_at = models.DateTimeField(
        verbose_name='Время получения сообщения',
        auto_now_add=True
    )

    def __str__(self):
        return f'Сообщения пользователя {self.profile.name}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщенеия'
