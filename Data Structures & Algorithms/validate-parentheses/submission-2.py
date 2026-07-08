class Solution:
    def isValid(self, s: str) -> bool:
        store = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for i in s:
            if i not in store:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if store[i] != stack[-1]:
                    return False
                stack.pop()
        return True