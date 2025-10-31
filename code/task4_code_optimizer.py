
import time
import numpy as np
import io
from datetime import datetime

# === Step 1: Simulated inefficient function ===
def inefficient_sum(numbers):
    """Simulates inefficient code using manual loops."""
    total = 0
    for n in numbers:
        total += n
    return total


# === Step 2: AI Optimization Suggestion (Simulated GPT Output) ===
ai_suggestion = """
AI Suggestion:
Instead of iterating manually through the list to compute a sum,
use NumPy's vectorized operations which are optimized in C.
Optimized version:
    def efficient_sum(numbers):
        return np.sum(numbers)
"""

print("=== AI in Software Engineering - Task 4: AI Code Optimization ===")
print("Simulating AI suggestion for optimizing a Python function...\n")
print(ai_suggestion)

# === Step 3: Optimized Function ===
def efficient_sum(numbers):
    """Optimized version using NumPy's built-in sum."""
    return np.sum(numbers)


# === Step 4: Compare performance ===
data = np.random.randint(1, 100, size=10_000_000)

start1 = time.time()
inefficient_sum(data)
t1 = time.time() - start1

start2 = time.time()
efficient_sum(data)
t2 = time.time() - start2

# === Step 5: Display comparison ===
print("\n=== Performance Comparison ===")
print(f"Inefficient Loop Method: {t1:.4f} seconds")
print(f"Efficient NumPy Method:  {t2:.4f} seconds")
print(f"Speed Improvement: {(t1/t2):.2f}x faster")

# === Step 6: Save results to file ===
results_file = "task4_results.txt"
with open(results_file, "w", encoding="utf-8") as f:
    f.write("=== Task 4: AI Code Optimization Results ===\n")
    f.write(f"Run timestamp: {datetime.now()}\n\n")
    f.write(ai_suggestion)
    f.write("\n=== Performance Comparison ===\n")
    f.write(f"Inefficient Loop: {t1:.4f} seconds\n")
    f.write(f"Efficient NumPy: {t2:.4f} seconds\n")
    f.write(f"Speed Improvement: {(t1/t2):.2f}x faster\n")

print(f"\n✅ Results saved to {results_file}")
