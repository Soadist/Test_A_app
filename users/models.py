from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    first_name = models.CharField(
        _('first name'),
        help_text=_('Required. 150 characters or fewer.'),
        max_length=150,
    )
    last_name = models.CharField(
        _('last name'),
        help_text=_('Required. 150 characters or fewer.'),
        max_length=150
    )
    email = models.EmailField(
        _('email address'),
        help_text=_('Required. 254 characters or fewer.'),
        max_length=254,
        unique=True,
        error_messages={
            'unique': _('A user with that e-mail already exists.'),
        },
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name'
    ]

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        ordering = ['id']
