class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o = {'{' : '}', '[' : ']', '(' : ')'}

        if not s:
            return False
        for p in s:
            if p in '{[(':
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                pop = stack.pop()
                if p != o[pop]:
                    return False
        return len(stack) == 0

