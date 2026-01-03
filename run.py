from core.llm_engine import generate_test_code, save_test_file
from core.selenium_runner import run_test
from transformers import pipeline

MODEL_NAME = "microsoft/phi-3-mini-4k-instruct"

pipe = pipeline("text-generation", model=MODEL_NAME, device_map="auto", dtype="auto")

print("🧠 AI + Selenium Test Generator 🧪\n")
scenario = input("Enter your test scenario: ")

prompt = f"""You are a Python Selenium expert.
Generate only valid Python code (no explanation) for this task:
{scenario}
Requirements:
- Use Chrome WebDriver
- Include waits where necessary
- End with print("✅ Test Passed") or print("❌ Test Failed")
"""

print("[INFO] Generating test case...")
response = pipe(prompt, max_new_tokens=600)[0]['generated_text']
code = generate_test_code(scenario, response)

file_path = save_test_file(scenario, code)
print(f"[INFO] Test case saved as: {file_path}")
run_test(file_path)