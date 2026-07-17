class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
             
        for i in range(len(nums)):
            delta = target - nums[i]
            if(hash.get(delta) != None):
                j = hash.get(delta)
                if(i != j):
                    return [min(i,j), max(i, j)]
        
        return None
        