import json

from journal.services.ai_service.ai_variables import (
    GPT_OSS_SYSTEM_MESSAGE,
    LLMClient,
    LLM_MODEL,
    TEMPERATURE,
    TOP_P,
    REASONING_EFFORT
)
from journal.services.ai_service.client import CLIENT


class AIService:

    """
    Service for interacting with configured LLM backends.
    Currently tuned for OpenAI GPT-OSS models.
    (openai/gpt-oss-120b, openai/gpt-oss-20b)
    """

    def __init__(
            self,
            system_message: str = GPT_OSS_SYSTEM_MESSAGE,
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

        """
        Convert a structured input into a formatted JSON string.
        """

        return json.dumps(
            user_input,
            ensure_ascii=False,
            indent=2
        )


    def _build_prompt(self, user_input: dict) -> dict:

        """
        Take user_input for formatting
        and return the payload for *.chat.completions.create()
        """


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

    def send(self, user_input: dict, llm_model: str | None = None) -> str:

        """
        Send a prompt to LLM and return completion.
        """

        prompt = self._build_prompt(user_input)

        if llm_model:
            prompt["model"] = llm_model

        completion = self._client.chat.completions.create(**prompt)



        return  json.loads(
            completion
            .choices[0]
            .message
            .content
        )