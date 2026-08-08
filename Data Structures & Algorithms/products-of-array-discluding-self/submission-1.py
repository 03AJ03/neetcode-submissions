class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)
        output = [1] * n

        # Products to the LEFT
        prefix = 1

        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Products to the RIGHT
        suffix = 1

        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output