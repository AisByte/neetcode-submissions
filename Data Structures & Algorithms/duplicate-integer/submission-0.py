class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dup_dict = {f'{j}':0 for j in nums}
        for i in nums:
            dup_dict[f'{i}'] = dup_dict[f'{i}'] + 1

        dup_list = [True for j in dup_dict if dup_dict[j] > 1]

        # check if there is True available
        return any(dup_list)

        

