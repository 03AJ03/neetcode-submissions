class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        l=0
        count={}
        max_freq=0
        len_max=0
        for r in range(n):
            count[s[r]]=count.get(s[r],0)+1
            max_freq=max(max_freq,count[s[r]])
            while (r-l+1)-max_freq>k:
                count[s[l]] -= 1
                l += 1
            len_max=max(len_max,r-l+1)
        return len_max

