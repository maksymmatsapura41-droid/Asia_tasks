"""
Two pointers + sliding window (simple examples).

1) Two pointers:
- opposite direction: left and right move toward each other
- same direction: read/write pointers move from left to right

2) Sliding window:
- fixed window size (k)
- dynamic window size (expand + shrink)
"""

from typing import Dict, List, Tuple


# -----------------------------
# Two pointers: simple examples
# -----------------------------
def reverse_string_in_place(chars: List[str]) -> None:
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap outer characters, then move toward the center.
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1


def two_sum_sorted(numbers: List[int], target: int) -> Tuple[int, int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        current = numbers[left] + numbers[right]
        if current == target:
            return left + 1, right + 1
        # Because array is sorted:
        # - if sum is too small, move left pointer right
        # - if sum is too large, move right pointer left
        if current < target:
            left += 1
        else:
            right -= 1
    return -1, -1


def move_zeroes(nums: List[int]) -> None:
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            # Place next non-zero value at write position.
            # If read == write, this keeps value in place.
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


# -----------------------------
# Sliding window: simple examples
# -----------------------------
def max_sum_subarray_k(nums: List[int], k: int) -> int:
    if k <= 0 or k > len(nums):
        raise ValueError("k must be in range 1..len(nums)")

    window_sum = sum(nums[:k])
    best = window_sum

    for right in range(k, len(nums)):
        # Add new right element and remove leftmost old element.
        window_sum += nums[right]
        window_sum -= nums[right - k]
        best = max(best, window_sum)

    return best


def min_subarray_len_at_least_target(target: int, nums: List[int]) -> int:
    left = 0
    current_sum = 0
    best = float("inf")

    for right in range(len(nums)):
        # Expand the window by moving right boundary.
        current_sum += nums[right]

        while current_sum >= target:
            # Window is valid: try to shrink it to get shorter length.
            best = min(best, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if best == float("inf") else int(best)


def length_of_longest_substring_no_repeat(text: str) -> int:
    left = 0
    best = 0
    freq: Dict[str, int] = {}

    for right in range(len(text)):
        ch = text[right]
        # Include current character into the window state.
        freq[ch] = freq.get(ch, 0) + 1

        while freq[ch] > 1:
            # Duplicate found: shrink from the left
            # until current character count becomes 1.
            left_ch = text[left]
            freq[left_ch] -= 1
            left += 1

        # Now window [left..right] has unique characters.
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    # Two pointers
    chars = list("algorithm")
    reverse_string_in_place(chars)
    print("Reverse String:", "".join(chars))

    i, j = two_sum_sorted([2, 7, 11, 15], 9)
    print("Two Sum II indices:", i, j)

    zeros = [0, 1, 0, 3, 12]
    move_zeroes(zeros)
    print("Move Zeroes:", zeros)

    # Sliding window
    print("Max sum (k=3):", max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3))
    print(
        "Min length sum >= 7:",
        min_subarray_len_at_least_target(7, [2, 3, 1, 2, 4, 3]),
    )
    print(
        "Longest substring without repeat:",
        length_of_longest_substring_no_repeat("abcabcbb"),
    )

