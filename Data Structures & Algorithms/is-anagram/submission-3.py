class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t): # anagram possible only if same length
            # sort the words and compare
            return sorted(list(s)) == sorted(list(t))
        else:
            return False

        


        
        