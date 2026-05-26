import json
from typing import Any

from journal.services.ai_service.ai_variables import (
    SYSTEM_MESSAGE,
    LLMClient,
    LLM_MODEL,
    TEMPERATURE,
    TOP_P,
    REASONING_EFFORT
)
from journal.services.ai_service.client import CLIENT


class AIService:
    def __init__(
            self,
            system_message: str = SYSTEM_MESSAGE,
            client: LLMClient = CLIENT,
            llm_model: str = LLM_MODEL,
            temperature: float = TEMPERATURE,
            top_p: float = TOP_P,
            reasoning_effort: str = REASONING_EFFORT,
            system_role_name: str = "system",
            user_role_name: str = "user",
    ) -> None:
        self._system_message = system_message
        self._client = client
        self._llm_model = llm_model
        self._temperature = temperature
        self._top_p = top_p
        self._reasoning_effort = reasoning_effort
        self._system_role_name = system_role_name
        self._user_role_name = user_role_name

    def _format_input(self, user_input: dict) -> str:
        return json.dumps(
            user_input,
            ensure_ascii=False,
            indent=2
        )


    def _build_prompt(self, user_input: dict) -> dict:
        prompt = {
            "model": self._llm_model,
            "messages": [
                {
                    "role": self._system_role_name,
                    "content": self._system_message,
                },
                {
                    "role": self._user_role_name,
                    "content": self._format_input(user_input),
                },
            ],
            "temperature": self._temperature,
            "top_p": self._top_p,
            "reasoning_effort": self._reasoning_effort,
        }

        return prompt

    def send(self, user_input: dict) -> Any:
        completion = self._client.chat.completions.create(**self._build_prompt(user_input))

        return completion