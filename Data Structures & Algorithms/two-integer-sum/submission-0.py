class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = dict()

        for i in range(len(nums)):
            to_find = target - nums[i]

            if to_find in d.keys():
                return [d[to_find], i]
            
            d[nums[i]] = i