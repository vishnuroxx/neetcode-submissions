class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        prefix = 1
        suffix = 1
        

        for idx in range(n):
            output[idx] = prefix
            prefix *= nums[idx]

        for idx in range(n-1, -1, -1):
            output[idx] *= suffix
            suffix *= nums[idx]

        
        return output 
        
        