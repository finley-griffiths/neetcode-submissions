class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(list(zip(position, speed)))
        for car in cars[::-1]:
            stack.append((target - car[0]) / car[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop(-1)
        return len(stack)
