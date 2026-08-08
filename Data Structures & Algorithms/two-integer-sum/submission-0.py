class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N=len(nums)
        for i in range(N):
            for j in range(i+1,N):
                if nums[j]==target-nums[i]:
                    return [i,j]
                

        