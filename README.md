# SelenoBrain

SelenoBrain is a small utility that combines a local LLM text-generation pipeline with Selenium to auto-generate and run end-to-end browser tests in Python.

Features
- Generate Python Selenium tests from a natural language scenario using an LLM pipeline.
- Automatically install the matching ChromeDriver via `chromedriver-autoinstaller`.
- Save generated test files to `generated_tests/` and execute them locally.

Project layout
- `run.py` — CLI entry that prompts for a scenario, asks the model to generate a test, saves it and runs it.
- `core/llm_engine.py` — helpers to extract, sanitize and save LLM-generated test code.
- `core/selenium_runner.py` — runs a generated test file in a subprocess and prints results.
- `generated_tests/` — directory where produced tests are saved.
- `requirements.txt` — Python dependencies.

Prerequisites
- Python 3.10+ (or a recent 3.x)
- Chrome browser installed on the system

Install
1. Create a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Usage
1. Run the generator:

```bash
python3 run.py
```

2. Enter a short natural-language scenario when prompted, for example:

"Open the staging site, log in as a test user, and verify the dashboard loads."

The tool will:
- Send a prompt to the configured model pipeline (see `run.py`).
- Extract Python code from the model response, inject `chromedriver-autoinstaller` if missing, and save to `generated_tests/`.
- Execute the generated test file and print output and errors.

Configuration notes
- The model pipeline is configured in `run.py` (the code uses a `transformers` pipeline). Adjust `MODEL_NAME` and pipeline settings there if you want a different model or device mapping.
- `core/llm_engine.py` performs simple extraction of Python code blocks from model output and appends a default failure print if none is present — review or harden this for production use.

Security and credentials
- Never hard-code real credentials into prompts or generated tests. Use environment variables or a secrets manager in real projects.

Troubleshooting
- If ChromeDriver issues appear, ensure Chrome is up-to-date; `chromedriver-autoinstaller` will try to pick the matching driver.
- If tests hang, check network access and increase timeouts where appropriate.

Contributing
- Improve prompts, add unit tests, or enhance code-safety checks in `core/llm_engine.py`.

License
- This repository does not include a license file. Add one if you plan to share this publicly.

---

If you'd like, I can also:
- Add an example scenario and a sample generated test in `generated_tests/`.
- Add CI/test runners or a `Makefile` to simplify common tasks.

