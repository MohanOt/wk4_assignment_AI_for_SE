"""
task1_sorting.py

Contains two functions to sort a list of dictionaries by a specified key:
1) sort_dicts_by_key_ai: concise idiomatic implementation (returns a new list)
2) sort_dicts_by_key_manual: robust manual implementation (sorts in-place and returns list)

Both functions accept:
- items: list of dicts
- key_name: key to sort by
- reverse: bool indicating descending order if True
"""

from typing import List, Dict, Any


def sort_dicts_by_key_ai(items: List[Dict[str, Any]], key_name: str, reverse: bool = False) -> List[Dict[str, Any]]:
   
    # Use .get(key_name, None) as key accessor so missing keys return None
    return sorted(items, key=lambda d: d.get(key_name, None), reverse=reverse)


def sort_dicts_by_key_manual(items: List[Dict[str, Any]], key_name: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Robust manual implementation:
    - Normalizes sort keys into tuples that establish a consistent ordering
      across missing values and mixed types.
    - Sorts the list in-place (to save memory) and returns it.

    Normalization tuple structure:
      (missing_flag, type_rank, normalized_value)
    where missing_flag: 1 for missing -> placed after present values by default
          type_rank: 0 for numeric, 1 for string, 2 for other
    """
    def normalize_value(value):
        # Missing values
        if value is None:
            return (1, 99, None)
        # Numeric types (int/float)
        if isinstance(value, (int, float)):
            return (0, 0, value)
        # Strings
        if isinstance(value, str):
            return (0, 1, value)
        # Booleans -> treat as ints
        if isinstance(value, bool):
            return (0, 0, int(value))
        # Fallback: convert to string
        return (0, 2, str(value))

    def sort_key(d: Dict[str, Any]):
        raw = d.get(key_name, None)
        return normalize_value(raw)

    # Sort in-place
    items.sort(key=sort_key, reverse=reverse)
    return items


# helper if module run directly 
if __name__ == "__main__":
    sample = [{"a": 3}, {"a": 1}, {"b": 2}, {"a": "2"}, {"a": None}, {"a": 2}]
    print("AI-style (new list):", sort_dicts_by_key_ai(sample, "a"))
    print("Manual (in-place):", sort_dicts_by_key_manual(sample.copy(), "a"))
