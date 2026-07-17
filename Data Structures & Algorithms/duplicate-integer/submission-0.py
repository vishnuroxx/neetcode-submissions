class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in nums:
            hash[i] = 0

        for i in nums:
            if(hash[i] == 0):
                hash[i] += 1 
            else:
                return True
      
        return False
        