from django.contrib import admin

from journal.models import JournalEntry, MoodTag, AIInsight, ReflectionSnapshot


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "user",
        "mood_score",
        "created_at",
    )

    search_fields = ("title", "content")
    list_filter = (
        "mood_score",
        "created_at",
    )


@admin.register(MoodTag)
class MoodTagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "emoji",
        "color",
    )

    search_fields = ("name",)


@admin.register(AIInsight)
class AIInsightAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "journal_entry",
        "created_at",
    )

    search_fields = (
        "journal_entry__title",
        "journal_entry__user__username",
    )

    list_filter = ("created_at",)


@admin.register(ReflectionSnapshot)
class ReflectionSnapshotAdmin(admin.ModelAdmin):
    pass
