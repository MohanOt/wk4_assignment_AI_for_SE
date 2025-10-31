# saves results into .txt file

import io
import sys
from datetime import datetime
from run_task1_demo import main as run_demo

def run_and_capture():
    # Redirect stdout to capture output
    buffer = io.StringIO()
    saved_stdout = sys.stdout
    sys.stdout = buffer

    print(f"=== AI in Software Engineering - Week 4 ===")
    print(f"Task 1: AI-Powered Code Completion (Sorting dictionaries)\n")
    print(f"Run timestamp: {datetime.now()}")
    print("-" * 60)

    try:
        run_demo()
        print("\n✅ Demo completed successfully.")
    except Exception as e:
        print(f"\n❌ Error running demo: {e}")
    finally:
        sys.stdout = saved_stdout

    output = buffer.getvalue()
    buffer.close()
    return output


def main():
    output = run_and_capture()
    # Save to file
    with open("task1_results.txt", "w", encoding="utf-8") as f:
        f.write(output)
    print("✅ Results saved to task1_results.txt\n")
    print("Preview (first 20 lines):")
    print("\n".join(output.splitlines()[:20]))


if __name__ == "__main__":
    main()
