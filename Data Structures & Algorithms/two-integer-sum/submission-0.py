class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_pair = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if i == j:
                    continue
                elif target == nums[i] + nums[j]:
                    return [i,j]

        