from llm.llm_client import HuggingFaceLLM


class ExecutorAgent:
    def __init__(self):
        self.llm = HuggingFaceLLM()

    def execute(self, plan):
        prompt = (
            "Write ONE short, attractive dating bio.\n"
            "Do NOT create a list.\n"
            "Do NOT repeat the instructions.\n"
            "Return only ONE bio.\n\n"
            f"Person description: {plan['user_query']}\n"
            "Dating bio:"
        )

        raw_output = self.llm.generate(prompt)

        # -------- CLEAN OUTPUT --------
        text = raw_output.strip()

        # Remove prompt leakage
        for junk in [
            "Write ONE short",
            "Person description:",
            "Dating bio:"
        ]:
            if junk in text:
                text = text.split(junk)[-1]

        # Remove URLs
        text = text.replace("http://", "").replace("https://", "")

        # Allow max 2 lines for better flow
        lines = text.split("\n")
        text = " ".join(lines[:2])

        # Length safety
        text = text.strip()[:450]

        # Fallback (very important)
        if len(text) < 40:
            text = (
                "Confident, thoughtful, and always open to meaningful conversations. "
                "I enjoy personal growth, good vibes, and building genuine connections."
            )

        return {
            "executed_steps": plan["steps"],
            "ai_output": text
        }
