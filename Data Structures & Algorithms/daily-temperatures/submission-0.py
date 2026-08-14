class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        Stack=[]
        for i,t in enumerate(temperatures):
            while Stack and temperatures[Stack[-1]]<t:
                prev_index=Stack.pop()
                result[prev_index]=i-prev_index
            Stack.append(i)

        return result
        