import os

models = ["chatgpt", "claude", "gemini", "deepseek", "grok", "phi4-mini", "qwen-7b"]

prompts = [
    # S1
    "S1-P1", "S1-P1-ADV",
    "S1-P2", "S1-P2-ADV",
    "S1-P3", "S1-P3-ADV",
    "S1-P4", "S1-P4-ADV",
    "S1-P5", "S1-P5-ADV",
    "S1-P6",
    # S2
    "S2-P1", "S2-P1-ADV",
    "S2-P2", "S2-P2-ADV",
    "S2-P3", "S2-P3-ADV",
    "S2-P4", "S2-P4-ADV",
    "S2-P5", "S2-P5-ADV",
    # S3
    "S3-P1", "S3-P1-ADV",
    "S3-P2", "S3-P2-ADV",
    "S3-P3", "S3-P3-ADV",
    "S3-P4", "S3-P4-ADV",
    "S3-P5",
    # S4
    "S4-P1", "S4-P1-ADV",
    "S4-P2", "S4-P2-ADV",
    "S4-P3", "S4-P3-ADV",
    "S4-P4", "S4-P4-ADV",
    "S4-P5", "S4-P5-ADV",
    # S5
    "S5-P1", "S5-P1-ADV",
    "S5-P2A", "S5-P2B", "S5-P2C", "S5-P2D",
    "S5-P3",
    "S5-P4", "S5-P4-ADV",
    "S5-P5", "S5-P5-ADV",
    # S6
    "S6-P1A", "S6-P1B",
    "S6-P2", "S6-P2-ADV",
    "S6-P3", "S6-P3-ADV",
    "S6-P4", "S6-P4-CON",
    "S6-P5", "S6-P5-ADV",
    "S6-P6", "S6-P6-ADV",
]

created = 0
for model in models:
    folder = os.path.join("responses", model)
    os.makedirs(folder, exist_ok=True)
    for prompt in prompts:
        filename = f"{model.replace('-', '').upper() if False else model.title().replace('-','').replace('4','4')}_{prompt}.txt"
        # Clean model name for filename: chatgpt -> ChatGPT, phi4-mini -> Phi4Mini etc.
        model_label = {
            "chatgpt":  "ChatGPT",
            "claude":   "Claude",
            "gemini":   "Gemini",
            "deepseek": "DeepSeek",
            "grok":     "Grok",
            "phi4-mini":"Phi4Mini",
            "qwen-7b":  "Qwen7B",
        }[model]
        filepath = os.path.join(folder, f"{model_label}_{prompt}.txt")
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"MODEL: {model_label}\n")
                f.write(f"PROMPT: {prompt}\n")
                f.write(f"DATE TESTED: \n")
                f.write("-" * 40 + "\n")
                f.write("RESPONSE:\n\n")
            created += 1

print(f"Done — {created} files created across {len(models)} model folders.")