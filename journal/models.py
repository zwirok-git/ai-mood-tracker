from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class User(AbstractUser):
    class Meta:
        ordering = [
            "-last_login",
        ]

class JournalEntry(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="entries",
    )

    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()

    mood_score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        help_text="0 = very low, 10 = excellent",
    )

    tags = models.ManyToManyField(
        to="MoodTag",
        related_name="entries",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]


class MoodTag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=7)
    emoji = models.CharField(max_length=32,)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.emoji} {self.name}"


class AIInsight(models.Model):
    journal_entry = models.OneToOneField(
        to=JournalEntry,
        on_delete=models.CASCADE,
        related_name="ai_insight",
    )

    summary = models.TextField()
    recommendations = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    emotions = models.JSONField(default=list)


class ReflectionSnapshot(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reflection"
    )

    summary = models.TextField()
    average_mood = models.FloatField()
    entries_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    top_emotions = models.JSONField(default=list)
