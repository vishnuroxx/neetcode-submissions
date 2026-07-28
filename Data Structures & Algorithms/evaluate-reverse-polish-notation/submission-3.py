class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "*", "-", "/"}
        stack = []
        for token in tokens: 
            if token in operands:
                print(stack)
                y = stack.pop()
                x = stack.pop()
                match token: 
                    case "+":
                        stack.append(x + y)
                    case "*":
                        stack.append(x * y)
                    case "/":
                        stack.append(int(x / y))
                    case _:
                        stack.append(x - y)
            else:
                stack.append(int(token))

        return stack.pop()

        