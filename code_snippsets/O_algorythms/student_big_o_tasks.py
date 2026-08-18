def task_1_last_element(items):
    if not items:
        return None
    return items[-1]


def task_2_sum_positive(items):
    total = 0
    for x in items:
        if x > 0:
            total += x
    return total


def task_3_reverse_string(text):
    result = ""
    for ch in text:
        result = ch + result
    return result


def task_4_has_pair_with_sum(items, target):
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            if items[i] + items[j] == target:
                return True
    return False


def task_5_count_unique(items):
    seen = set()
    for x in items:
        seen.add(x)
    return len(seen)


def task_6_repeat_halving(number):
    steps = 0
    while number > 1:
        number //= 2
        steps += 1
    return steps


def run_practice():
    data = [7, 3, 9, 1, 3, 8, -2]
    text = "algorithm"

    tasks = [
        ("task_1_last_element", task_1_last_element, (data,)),
        ("task_2_sum_positive", task_2_sum_positive, (data,)),
        ("task_3_reverse_string", task_3_reverse_string, (text,)),
        ("task_4_has_pair_with_sum", task_4_has_pair_with_sum, (data, 10)),
        ("task_5_count_unique", task_5_count_unique, (data,)),
        ("task_6_repeat_halving", task_6_repeat_halving, (256,)),
    ]

    print("=== Big O practice tasks ===")
    for idx, (name, fn, args) in enumerate(tasks, start=1):
        print(f"{idx}. {name:<24} -> result: {fn(*args)}")

    print("\nYour goal: define Big O for each task.")


if __name__ == "__main__":
    run_practice()
