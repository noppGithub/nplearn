class Solution:
    def isValid(self, s: str) -> bool:
        """manage the opening brackets, in each closing bracket,
        get ahead of the stack and check the match
        """
        stack = []
        match = {")": "(", "]": "[", "}": "{"}
        for character in s:
            if character in match:
                if not stack or stack.pop() != match[character]:
                    return False
            else:
                stack.append(character)
        return not stack
    def isValid2(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if i == ")" and stack[-1] == "(":
                        stack.pop()
                    elif i == "]" and stack[-1] == "[":
                        stack.pop()
                    elif i == "}" and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False

