class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        prefix = 1
        suffix = 1
        

        for idx in range(n):
            output[idx] = prefix
            prefix *= nums[idx]

        for idx in range(1,n):
            output[n-idx] *= suffix
            suffix *= nums[n-idx]

        output[0] *= suffix
        
        return output 
        
        