from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dot = max(nums)
        cur_min, cur_max = 1, 1
        
        for n in nums:
            tmp = n * cur_max
            cur_max = max(n*cur_max, n*cur_min, n)
            cur_min = min(tmp, n*cur_min, n)        
            max_dot = max(max_dot, cur_max)
        return max_dot