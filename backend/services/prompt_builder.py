from pathlib import Path


class PromptBuilder:
    def __init__(self, prompts_dir: str):
        self.prompts_dir = Path(prompts_dir)

        # Load system prompt (behavior + rules)
        self.system_prompt = (
            self.prompts_dir / "system_prompt.txt"
        ).read_text(encoding="utf-8")

        # Load output format (strict structure)
        self.output_format = (
            self.prompts_dir / "output_format.txt"
        ).read_text(encoding="utf-8")

        # Load user prompt template (dynamic inputs)
        self.user_prompt_template = (
            self.prompts_dir / "user_prompt.txt"
        ).read_text(encoding="utf-8")

    def get_system_prompt(self) -> str:
        """
        Returns system-level instructions (role + rules)
        """
        return self.system_prompt

    def build_prompt(self, input_data: dict) -> str:
        """
        Builds the final user prompt by combining:
        - Candidate/job data
        - Output formatting instructions
        """

        user_context = self.user_prompt_template.format(
            job_role=input_data.get("job_role"),
            candidate_experience_level=input_data.get("candidate_experience_level"),
            job_description=input_data.get("job_description"),
            interview_question=input_data.get("interview_question"),
            candidate_answer=input_data.get("candidate_answer"),
        )

        # Final prompt sent as USER message
        final_prompt = f"""
{user_context}

{self.output_format}
"""
        return final_prompt.strip()
