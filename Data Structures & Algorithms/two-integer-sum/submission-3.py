class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            if (b := target - value) in seen: # walrus operator -> assign and compare in same line
                return [seen[b], i] # if seen immediately return
            seen[value] =  i

