class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False

                if stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False

        return not stack

    # Результат LeetCode: 1 ms, 19,39 MB