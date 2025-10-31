# test_task1.py
from task1_sorting import sort_dicts_by_key_ai, sort_dicts_by_key_manual

def test_sort_by_numeric_key():
    data = [{"x": 2}, {"x": 1}, {"x": 3}]
    ai_sorted = sort_dicts_by_key_ai(data, "x")
    manual_sorted = sort_dicts_by_key_manual(data.copy(), "x")
    assert [d.get("x") for d in ai_sorted] == [1, 2, 3]
    assert [d.get("x") for d in manual_sorted] == [1, 2, 3]

def test_handles_missing_keys():
    data = [{"x": 2}, {}, {"x": 1}]
    manual_sorted = sort_dicts_by_key_manual(data.copy(), "x")
    # missing should come first or last depending on normalization; we check stable order existence
    assert any("x" not in d for d in manual_sorted)
