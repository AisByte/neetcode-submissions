class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # slice based on the index and multiply the remaining
        output = [math.prod(nums[:i] + nums[i+1:]) for i in range(0,len(nums))]

        return output
















        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        
        # prefix[i] = product of nums[0..i-1]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # suffix[i] = product of nums[i+1..n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        # output[i] = prefix[i] * suffix[i]
        return [prefix[i] * suffix[i] for i in range(n)]
        
        