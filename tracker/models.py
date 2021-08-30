from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Report(models.Model):
    ACTIVITY_TYPE = [
        ('bike', 'Велосипед'),
        ('walking', 'Ходьба'),
        ('running', 'Бег')
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reports'
    )
    start_datetime = models.DateTimeField(
        auto_now_add=False,
        verbose_name='Дата и время начала активности',
        blank=False
    )
    end_datetime = models.DateTimeField(
        auto_now_add=False,
        verbose_name='Дата и время окончания активности',
        blank=False
    )
    activity_type = models.CharField(
        max_length=9,
        choices=ACTIVITY_TYPE,
        blank=False
    )
    distance = models.PositiveIntegerField(
        verbose_name='Расстояние',
        blank=False
    )
    calories = models.PositiveIntegerField(
        verbose_name='Количество калорий',
        blank=False
    )

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'

    def __str__(self):
        return (
            str(self.user.username) + ' '
            + str(self.activity_type) + ' '
            + str(self.distance) + ' м'
        )
