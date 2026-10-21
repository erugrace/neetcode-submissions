class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res  = 0
        chardict = {}
        l = 0
        for r in range(len(s)):
            chardict[s[r]] = 1 + chardict.get(s[r], 0)
            maxF = max(chardict.values())
            if (r-l+1) - maxF <= k:
                res = r-l+1
            else:
                chardict[s[l]] -=1
                l+= 1
                
        return res




        