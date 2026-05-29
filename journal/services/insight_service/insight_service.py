from django.db import transaction

from journal.models import AIInsight, JournalEntry

from journal.services.ai_service.ai_service import AIService


class InsightService:
    def __init__(self, ai_service: type[AIService] = AIService) -> None:
        self._ai_service = ai_service()

    def generate_insight(
        self,
        entry: JournalEntry,
        regenerate: bool = False,
        llm_model: str | None = None,
    ) -> AIInsight:
        response = self._ai_service.send(
            user_input={
                "title": entry.title,
                "content": entry.content,
                "mood_score": entry.mood_score,
            },
            llm_model=llm_model,
        )

        with transaction.atomic():
            locked = JournalEntry.objects.select_for_update().get(pk=entry.pk)

            if not regenerate and hasattr(locked, "ai_insight"):
                return locked.ai_insight

            insight, _ = AIInsight.objects.update_or_create(
                journal_entry=locked,
                defaults={
                    "summary": response["summary"],
                    "emotions": response["emotions"],
                    "recommendations": response["recommendations"],
                },
            )

        return insight
