class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 1:
            dp = [0 for i in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            if len(nums) > 2: 
                for idx in range(2, len(nums)):
                    dp[idx] = max(nums[idx] + dp[idx - 2], dp[idx - 1])

            return dp[-1]
        else:
            return nums[-1]
        