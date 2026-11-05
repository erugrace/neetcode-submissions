class Solution:
    def isValid(self, s: str) -> bool:
        chardict = {"}" : "{", ")":"(","]":"["}
        stack = []
        for char in s:
            if char in chardict:
                if stack and chardict[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True
        