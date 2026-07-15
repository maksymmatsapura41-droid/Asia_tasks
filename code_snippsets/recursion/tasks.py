"""
1.Условие: Напиши рекурсивную функцию, которая выводит числа от 1 до n, а затем от n до 1. Использовать циклы нельзя.
mirror_print(3)
# 3 2 1 1 2 3

2. Условие: Напиши рекурсивную функцию, которая возвращает количество гласных букв (a, e, i, o, u) в строке.
count_vowels("apple")
# 2

3. Проверка на палиндром
Условие: Напишите рекурсивную функцию, которая определяет, является ли строка палиндромом.
is_palindrome("radar")
# True

is_palindrome("hello")
# False
----------------------------------------
https://leetcode.com/problems/reverse-linked-list/description/

https://leetcode.com/problems/remove-linked-list-elements/description/
"""

def mirror_print(n):
    if n == 0:
        return
    print(n)
    mirror_print(n - 1)
    print(n)

# mirror_print(3)
total = 0
def count_vowels(w):
    if not w:
        return 0
    is_vowel = 1 if w[0] in 'aeiou' else 0
    return count_vowels(w[1:]) + is_vowel

# print(count_vowels("apple"))

def is_palindrome(w):
    if w[0].lower() != w[-1].lower():
        return False
    if len(w) <= 1:
        return True
    return is_palindrome(w[1:-1])
    
print(is_palindrome("r"))
print(is_palindrome("radar"))
print(is_palindrome("hello"))
print(is_palindrome("oello"))