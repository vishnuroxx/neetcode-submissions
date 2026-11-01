class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        state_variables = [0, 0, []]
        stack = [state_variables]
        while stack:
            curr_state = stack.pop()
            if curr_state[0] < len(nums) and curr_state[1] <= target:
                if curr_state[1] == target:
                    result.append(curr_state[2])
                else:
                    keep_array = curr_state[2].copy()
                    keep_array.append(nums[curr_state[0]])
                    throw_array = curr_state[2].copy()
                    next_state_keep = [curr_state[0], curr_state[1] + nums[curr_state[0]], keep_array]
                    next_state_throw = [curr_state[0] + 1, curr_state[1], throw_array] 
                    stack.append(next_state_throw)
                    stack.append(next_state_keep)
                    
   
        return result
                
            