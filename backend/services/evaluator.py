from services.prompt_builder import PromptBuilder
from services.llm_client import LLMClient


class InterviewEvaluator:
    """
    Orchestrates prompt building and LLM evaluation
    for a single interview answer (v1).
    """

    def __init__(
        self,
        prompts_dir: str,
        model_name: str,
        temperature: float = 0.3
    ):
        self.prompt_builder = PromptBuilder(prompts_dir)
        self.llm_client = LLMClient(
            model_name=model_name,
            temperature=temperature
        )

    def evaluate(self, input_data: dict) -> str:
        """
        Evaluates a single interview answer using GenAI.

        Steps:
        1. Load system-level instructions
        2. Build structured user prompt
        3. Send both to the LLM
        """

        system_prompt = self.prompt_builder.get_system_prompt()
        user_prompt = self.prompt_builder.build_prompt(input_data)

        response = self.llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )

        return response
