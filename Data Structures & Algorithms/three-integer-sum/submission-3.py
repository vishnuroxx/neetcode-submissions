class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array O(nlogn)
        nums.sort() 
        result = []
        for i in range(len(nums)): # 0 to 1
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            # 2 pointer
            while left < right:
                
                
                summation = nums[left] + nums[right]
                if summation < target:
                    left += 1
                elif summation > target: 
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1
                    while nums[right + 1] == nums[right] and left < right:
                        right -= 1
                    
        return result

                 
        