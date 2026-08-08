class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        N=nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False

        # N=len(nums)
        # for i in range(N):
        #     for j in range(i + 1, N):
        #         if nums[i]==nums[i+1]:
        #             return True
        # return False
                    

        