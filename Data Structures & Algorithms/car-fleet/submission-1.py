class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        cars = [] #(position, speed)

        for i in range(n):
            pos, sp = position[i], speed[i]
            cars.append((pos, sp))
        
        cars.sort(key=lambda x: x[0], reverse=True)

        stack = []

        for car in cars:
            pos, sp = car[0], car[1]
            time = (target - pos) / sp
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        
        return len(stack)

