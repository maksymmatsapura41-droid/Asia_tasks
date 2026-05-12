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
            window[s[i]] = window.get(s[i], 0) + 1
            window[s[i - k]] -= 1
            if window[s[i - k]] == 0:
                del window[s[i - k]]
            if len(window) == k:
                count += 1
        return count


obj = Solution()
res = obj.countGoodSubstrings("aababcabc")
print(res)
