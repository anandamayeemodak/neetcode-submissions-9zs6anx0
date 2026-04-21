class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) > 0:
                    top = stack.pop()
                    if (char == ")" and top == "(") or (char == "}" and top == "{") or (char == "]" and top == "["):
                        continue
                    else:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

        