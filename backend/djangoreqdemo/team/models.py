from django.db import models
import django.core
import django.db


class Team(
    django.db.models.Model,
):
    title = django.db.models.CharField(
        max_length=150,
        verbose_name="название",
        help_text="max 150 символов",
        unique=True,
    )
    country = django.db.models.CharField(
        max_length=150,
        verbose_name="страна",
        help_text="max 150 символов",
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
