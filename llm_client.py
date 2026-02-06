from transformers import pipeline

class HuggingFaceLLM:
    def __init__(self):
        # Stable local text-generation model
        self.pipe = pipeline(
            task="text-generation",
            model="distilgpt2"
        )

    def generate(self, prompt, max_tokens=200):
        result = self.pipe(
            prompt,
            max_new_tokens=max_tokens,
            do_sample=False,          # 🔑 IMPORTANT: repetition band
            num_return_sequences=1,
            truncation=True
        )

        text = result[0]["generated_text"]

        # 🔧 Prompt removal (taaki instruction repeat na ho)
        if text.startswith(prompt):
            text = text[len(prompt):]

        return text.strip()
