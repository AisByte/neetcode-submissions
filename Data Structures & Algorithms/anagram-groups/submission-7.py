class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        a = ord('a') # caching once
        for s in strs:
            count =  [0] * 26  #fixed alphabets
            for c in s:
                count[ord(c) - a] += 1
            groups[tuple(count)].append(s) # tuple for hashable key

        return(list(groups.values()))