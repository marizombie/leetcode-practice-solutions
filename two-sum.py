from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        
        for i, n in enumerate(nums):
            dif = target - n
            if dif in nums_dict:
                return [i, nums_dict[dif]]
            else:
                nums_dict[n] = i