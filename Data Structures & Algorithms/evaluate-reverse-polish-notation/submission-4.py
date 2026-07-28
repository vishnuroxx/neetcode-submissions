class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens: 
            match token: 
                case "+":
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(x + y)
                case "*":
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(x * y)
                case "/":
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(int(x / y))
                case "-":
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(x - y)
                case _:
                    stack.append(int(token))

                

        return stack.pop()

        