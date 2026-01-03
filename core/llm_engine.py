import re
from datetime import datetime
from pathlib import Path

def inject_autoinstaller_and_logging(code: str) -> str:
    """
    Ensures every generated Selenium test includes:
    - chromedriver-autoinstaller
    - proper logging
    - safe driver quit
    """
    # Avoid duplication if already injected
    if "chromedriver_autoinstaller" not in code:
        preamble = (
            "import chromedriver_autoinstaller\n"
            "chromedriver_autoinstaller.install()\n"
        )
        code = preamble + "\n" + code

    # Guarantee print logging for success/failure
    if 'print("✅ Test Passed")' not in code and 'print("❌ Test Failed")' not in code:
        code += "\nprint('❌ Test Failed')"

    return code


def generate_test_code(scenario: str, model_response: str) -> str:
    """
    Extract only valid Python code from LLM output and enhance it.
    """
    match = re.search(r"```python(.*?)```", model_response, re.DOTALL)
    code = match.group(1).strip() if match else model_response.strip()
    return inject_autoinstaller_and_logging(code)


def save_test_file(scenario: str, code: str) -> str:
    """
    Save test case to a unique file (sanitized name).
    """
    safe_name = re.sub(r'[^a-zA-Z0-9_\-]', '_', scenario.lower())[:50]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{safe_name}_{timestamp}.py"
    test_dir = Path("generated_tests")
    test_dir.mkdir(exist_ok=True)
    file_path = test_dir / filename
    file_path.write_text(code)
    return str(file_path)