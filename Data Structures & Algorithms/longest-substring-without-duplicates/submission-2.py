class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Charset=set()
        n=len(s)
        l=0
        result=0
        for r in range(n):
            while s[r] in Charset:
                Charset.remove(s[l])
                l+=1
            Charset.add(s[r])
            result=max(result,r-l+1)
        return result

        