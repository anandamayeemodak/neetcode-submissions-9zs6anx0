#Stack + truncate towards '0' not floor division
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_map = {"+": 1, "-": 2, "*": 3, "/": 4}

        for token in tokens:
            if token in operator_map:
                num1 = stack.pop()
                num2 = stack.pop()
                res = 0
                match operator_map[token]:
                    case 1:
                        res = num1 + num2
                    case 2:
                        res = num2 - num1
                    case 3:
                        res = num1 * num2
                    case 4:
                        res = float(num2) / num1
                stack.append(int(res))
            else:
                stack.append(int(token))
            print(stack)
        
        print(stack)
        return stack[-1]
        