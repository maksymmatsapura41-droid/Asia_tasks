import time
import random
import itertools
# -----------------------------
# O(1) - Constant
# -----------------------------
def o1_access(arr):
    # Return the first element (constant work).
    return arr[0] if arr else None
# -----------------------------
# O(log n) - Binary search
# -----------------------------
def ologn_binary_search(sorted_arr, target):
    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return True
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
# -----------------------------
# O(n) - Linear count
# -----------------------------
def on_sum(arr):
    count = 0
    for x in arr:
        if x % 2 == 0:
            count += 1
    return count
# -----------------------------
# O(n log n) - Sorting
# -----------------------------
def onlogn_sort(arr):
    return sorted(arr)
# -----------------------------
# O(n^2) - Double loop
# -----------------------------
def on2_pairs(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            count += 1
    return count

[1, 2, 3, 4, 5, 6, 7]
# -----------------------------
# O(n^3) - Triple loop
# -----------------------------
def on3_triples(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    return count
# -----------------------------
# O(2^n) - All subsets count
# -----------------------------
def o2n_subsets_count(items):
    n = len(items)
    count = 0
    for mask in range(1 << n):
        # One mask = one subset.
        _ = mask
        count += 1
    return count

# ["a", "b" ,"c"]
# (000) - mask(0) - {}
# (001) - mask(1) - {a}
# (010) - mask(2) - {b}
# (011) - mask(3) - {a,b}
# (100) - {c}
# (101) - {a,c}
# {110} - {b,c}
# {111} - {a, b, c}
# -----------------------------
# O(n!) - All permutations count
# -----------------------------
def on_fact_permutations_count(items):
    count = 0
    for _ in itertools.permutations(items):
        count += 1
    return count
def measure_time(func, *args, repeats=1):
    """
    Measure average execution time in milliseconds.
    """
    start = time.perf_counter()
    for _ in range(repeats):
        func(*args)
    end = time.perf_counter()
    return (end - start) * 1000 / repeats  # ms
def print_table(title, rows):
    print(f"\n{title}")
    print("-" * len(title))
    print(f"{'n':>8} | {'time (ms)':>12}")
    print("-" * 24)
    for n, t in rows:
        print(f"{n:>8} | {t:>12.4f}")


if __name__ == "__main__":
    random.seed(42)
    # 1) O(1)
    rows = []
    for n in [10, 100, 1_000, 10_000, 100_000]:
        arr = list(range(n))
        t = measure_time(o1_access, arr, repeats=20_000)
        rows.append((n, t))
    print_table("O(1) first element", rows)
    # 2) O(log n)
    rows = []
    for n in [10, 100, 1_000, 10_000, 100_000]:
        arr = list(range(n))
        target = n - 1
        t = measure_time(ologn_binary_search, arr, target, repeats=20_000)
        rows.append((n, t))
    print_table("O(log n) binary search (contains)", rows)
    # 3) O(n)
    rows = []
    for n in [100, 1_000, 10_000, 100_000]:
        arr = list(range(n))
        t = measure_time(on_sum, arr, repeats=200)
        rows.append((n, t))
    print_table("O(n) count even numbers", rows)
    # 4) O(n log n)
    rows = []
    for n in [100, 1_000, 5_000, 10_000]:
        arr = [random.randint(0, 1_000_000) for _ in range(n)]
        t = measure_time(onlogn_sort, arr, repeats=20)
        rows.append((n, t))
    print_table("O(n log n) sort", rows)
    # 5) O(n^2)
    rows = []
    for n in [50, 100, 200, 400]:
        arr = list(range(n))
        t = measure_time(on2_pairs, arr, repeats=3)
        rows.append((n, t))
    print_table("O(n^2) double loop", rows)
    # 6) O(n^3)
    rows = []
    for n in [20, 30, 40, 50]:
        arr = list(range(n))
        t = measure_time(on3_triples, arr, repeats=1)
        rows.append((n, t))
    print_table("O(n^3) triple loop", rows)
    # 7) O(2^n)
    rows = []
    for n in [10, 12, 14, 16, 18]:
        items = list(range(n))
        t = measure_time(o2n_subsets_count, items, repeats=1)
        rows.append((n, t))
    print_table("O(2^n) subsets", rows)
    # 8) O(n!)
    rows = []
    for n in [7, 8, 9, 10]:
        items = list(range(n))
        t = measure_time(on_fact_permutations_count, items, repeats=1)
        rows.append((n, t))
    print_table("O(n!) permutations", rows)
    print("\nDone.")