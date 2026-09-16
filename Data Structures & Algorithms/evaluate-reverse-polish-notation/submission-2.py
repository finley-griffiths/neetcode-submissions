class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in '+-*/':  # is an operand
                stack.append(int(t))
            else:  # is an operator
                o2, o1 = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(o1 + o2)
                elif t == '-':
                    stack.append(o1 - o2)
                elif t == '*':
                    stack.append(o1 * o2)
                else:
                    stack.append(int(o1 / o2))
        return stack[-1]