from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ["-last_login",]


class AIStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    PROCESSING = "PROCESSING", "Processing"
    COMPLETE = "COMPLETE", "Complete"
    FAILED = "FAILED", "Failed"


class JournalEntry(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="entries",
    )

    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()

    mood_score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ai_status = models.CharField(choices=AIStatus, default=AIStatus.PENDING)

    class Meta:
        ordering = ["-created_at"]


class MoodTag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    journal_entry = models.ManyToManyField(to=JournalEntry, related_name="tags")
    emoji = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]


class AIInsight(models.Model):
    journal_entry = models.OneToOneField(
        to=JournalEntry,
        on_delete=models.CASCADE,
        related_name="ai_insight",
    )

    summary = models.TextField()

    emotions = models.JSONField()

    recommendations = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)