class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def helper(curr, n, temp_sum, temp):
            nonlocal target, nums, result
            next_temp_1 = temp.copy() if temp else []
            next_temp_2 = temp.copy() if temp else []
            if curr < n:
                if temp_sum > target:
                    return
                elif temp_sum == target:
                    result.append(temp)
                    return
                else:
                    next_temp_2.append(nums[curr])
                    helper(curr + 1, n, temp_sum, next_temp_1)
                    helper(curr, n, temp_sum + nums[curr],
                            next_temp_2)
        helper(0, len(nums), 0, [])
   
        return result
                
            