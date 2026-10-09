class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        dict = {}
        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        for char in t:
            if char not in dict or dict[char] == 0:
                return False
            else:
                dict[char] -= 1
        return True
        