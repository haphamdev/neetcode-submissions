class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for t in tokens:
            if t in operators:
                right = stack.pop()
                left = stack.pop()
                result = 0
                match t:
                    case '+':
                        result = left + right
                    case '-':
                        result = left - right
                    case '*':
                        result = left * right
                    case _:
                        result = int(left / right)
                stack.append(result)
            else:
                stack.append(int(t))
        return stack[0]
        