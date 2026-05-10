class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict =  Counter(nums)
        result = []

        #bucket sorting
        bucket_list = [[] for _ in range(len(nums) + 1)]

        for num, count in freq_dict.items():
            bucket_list[count].append(num) # index = frequency
        for i in range(len(bucket_list) - 1, 0, -1): # iter from last (from largest)
            for num in bucket_list[i]:
                result.append(num)
                if k == len(result):
                    return result

        return result

        