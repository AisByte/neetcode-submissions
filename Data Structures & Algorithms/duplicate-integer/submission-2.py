class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set removes duplicates, after removing duplicates if length is less than original, then true
        return len(set(nums)) < len(nums)

        

