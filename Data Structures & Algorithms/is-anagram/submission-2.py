class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash= {} 
        if(len(s) > len(t)):
            s,t = t,s
        for char in s:
            if(hash.get(char) == None):
                hash[char] = 1
            else:
                hash[char] += 1

        for char in t:
            if(hash.get(char) == None or hash.get(char) == 0):
                return False 
            else:
                hash[char] -= 1

        return True 

        