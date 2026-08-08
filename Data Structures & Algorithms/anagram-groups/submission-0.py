from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:
            sortedwords=''.join(sorted(s))
            result[sortedwords].append(s)
        return list(result.values())

