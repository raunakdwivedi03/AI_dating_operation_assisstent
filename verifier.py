class VerifierAgent:
    def __init__(self):
        pass

    def verify(self, execution_result):
        return {
            "verified": True,
            "final_response": execution_result["ai_output"]
        }
