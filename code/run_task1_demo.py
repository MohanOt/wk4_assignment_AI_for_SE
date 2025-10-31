"""
run_task1_demo.py

Demonstrates both sorting functions and prints clear outputs
compares easily results and timing.
"""

import time
from task1_sorting import sort_dicts_by_key_ai, sort_dicts_by_key_manual

# Example dataset with mixed types and missing keys
dataset = [
    {"id": 1, "score": 10},
    {"id": 2, "score": None},
    {"id": 3},                     # missing 'score'
    {"id": 4, "score": 7},
    {"id": 5, "score": "5"},       # string value
    {"id": 6, "score": 3.5},
    {"id": 7, "score": 10},
    {"id": 8, "score": True},      # boolean value
]

def print_pretty(title, lst):
    print("\n" + "="*10 + f" {title} " + "="*10)
    for item in lst:
        print(item)
    print("="*30 + "\n")

def main():
    print("Original dataset:")
    print_pretty("Original", dataset)

    # AI-style: returns new list
    t0 = time.time()
    ai_sorted = sort_dicts_by_key_ai(dataset, "score", reverse=False)
    t1 = time.time()
    print_pretty(f"AI-suggested result (time {t1-t0:.6f}s)", ai_sorted)

    # Manual: in-place sort on a copy
    data_copy = [d.copy() for d in dataset]
    t2 = time.time()
    manual_sorted = sort_dicts_by_key_manual(data_copy, "score", reverse=False)
    t3 = time.time()
    print_pretty(f"Manual result (time {t3-t2:.6f}s)", manual_sorted)

    print("Notes:")
    print("- AI-style uses sorted() and may error if Python cannot compare mixed types.")
    print("- Manual normalizes values into a consistent order and handles missing values.")

if __name__ == "__main__":
    main()
