class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(ptr, curr, total_sum):
            if total_sum > target or ptr >= len(nums):
                return
            
            if total_sum == target:
                result.append(curr.copy())
                return

            curr.append(nums[ptr])
            dfs(ptr, curr, total_sum + nums[ptr])
            curr.pop()
            dfs(ptr+1, curr, total_sum)
            
        dfs(0,[],0)
   
        return result
                
            