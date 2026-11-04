class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        

        for idx in range(1, n):
            prefix[idx] = prefix[idx-1]*nums[idx-1]
            postfix[idx] = postfix[idx-1]*nums[n-idx]

        output = []
        l = 0 
        r = n - 1
   
        while l < n:
            output.append(prefix[l] * postfix[r])
            l += 1
            r -= 1

        return output 
        
        