class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cum_sum = 0
        for num in nums:
            cum_sum += num 
            max_sum = max(max_sum, cum_sum)
            if cum_sum < 0: 
                cum_sum = 0 # reset 
        return max_sum