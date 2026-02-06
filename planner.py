import json
from llm.llm_client import HuggingFaceLLM


class PlannerAgent:
    def __init__(self):
        pass

    def create_plan(self, user_input):
        """
        Deterministic planner (LLM-free).
        GPT-2 JSON ke liye reliable nahi hota,
        isliye plan hum code se bana rahe hain.
        """

        plan = {
            "user_query": user_input,
            "steps": [
                {"action": "analyze_user_intent"},
                {"action": "generate_dating_response"}
            ]
        }

        return plan
