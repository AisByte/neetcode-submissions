class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            if (b := target - value) in seen: # walrus operator 
                return [seen[b], i]
            seen[value] =  i

