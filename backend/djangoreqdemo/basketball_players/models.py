import django.core
import django.db.models


class BasketballPlayers(
    django.db.models.Model,
):
    
    name = django.db.models.CharField(
        max_length=150,
        verbose_name="имя",
        help_text="max 150 символов",
        unique=True,
    )
    age = django.db.models.PositiveIntegerField(
        "возраст",
    )
    team = django.db.models.CharField(
        "команда",
        max_length=100,
    )
    created = django.db.models.DateTimeField(
        "дата создания",
        auto_now_add=True,
        null=True,
    )
    career = django.db.models.BooleanField(
        "карьера",
        help_text="продолжает карьеру",
        default=True,
        null=True,
    )
    updated = django.db.models.DateTimeField(
        "дата изменения",
        auto_now=True,
        null=True,
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "питательное вещество"
        verbose_name_plural = "питательные вещества"

    def __str__(self):
        return self.title
