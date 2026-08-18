# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str):
        k = 3
        count = 0
        window = {}
        for el in s[:k]:
            window[el] = window.get(el, 0) + 1
        if len(window) == k:
            count += 1        
        for i in range(k, len(s)):
            left_char = s[i - k]
            right_char = s[i]
            window[right_char] = window.get(right_char, 0) + 1
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if len(window) == k:
                count += 1
        return count


obj = Solution()
res = obj.countGoodSubstrings("aababcabc")
print(res)
