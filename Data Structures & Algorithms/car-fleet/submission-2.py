class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        for x in range(len(position)):
            time=(target-position[x])/speed[x]
            stack.append((position[x],time))
        stack.sort(reverse=True)
        fleets = 0
        time_taken = 0
        for pos, time in stack:
            if time > time_taken:
                fleets += 1
                time_taken = time
        return fleets

        
