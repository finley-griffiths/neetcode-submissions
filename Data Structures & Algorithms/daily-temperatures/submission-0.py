class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
            elif temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    prev = stack.pop(-1)
                    prev_index = prev[1]
                    prev = prev[0]
                    result[prev_index] = i - prev_index
                stack.append((temperatures[i], i))
        return result