import subprocess

def run_test(file_path: str):
    try:
        result = subprocess.run(
            ["python3", file_path],
            capture_output=True,
            text=True,
            timeout=120
        )
        print(result.stdout)
        if result.stderr:
            print("🔍 Error log:\n", result.stderr)
        if result.returncode == 0:
            print("✅ Test executed successfully")
        else:
            print("❌ Test execution failed")
    except subprocess.TimeoutExpired:
        print("❌ Test execution timed out")
