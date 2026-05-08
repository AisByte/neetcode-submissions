class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, value in enumerate(nums):
            b = target - value
            if b in seen: 
                return [seen[b], i]
            seen[value] =  i

