class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted_words = sorted(strs, key=len)
        # from collections import defaultdict
        groups = defaultdict(list)

        for s in strs:
            count =  [0] * 26  #fixed alphabets
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s) # tuple for hashable key

        return(list(groups.values()))