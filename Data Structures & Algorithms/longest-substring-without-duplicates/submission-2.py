class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0 
        left,right = 0,0
        hash = {}
        while right < len(s):
            # check hash table
            if hash.get(s[right]) != None and hash.get(s[right]) >= left:
                left = hash[s[right]] + 1
             
            hash[s[right]] = right 
            # check the count and update accordingly 
            maxCount = max(right - left + 1, maxCount)
            # consume next letter
            right += 1
        return maxCount 

        
        