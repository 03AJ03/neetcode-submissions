class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        maxL=0
        maxR=0
        result=0
        while left<right:
            if height[left]<height[right]:
                if maxL<=height[left]:
                    maxL=height[left]
                else:
                    result+=maxL-height[left]
                left+=1
            else:
                if maxR<=height[right]:
                    maxR=height[right]
                else:
                    result+=maxR-height[right]
                right-=1
        return result


