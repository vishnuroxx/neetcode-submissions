class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash = {}
        for ch in s1:
            hash[ch] = hash.get(ch, 0) + 1

        left, right = -1, 0 
        characters = {}
        
        while right < len(s2):
            print(left, right)
            if hash.get(s2[right]):
                if characters.get(s2[right],0) + 1 <= hash[s2[right]]:
                    characters[s2[right]] = characters.get(s2[right],0) + 1
                    if left == -1:
                        left = right
                        
                    if right - left + 1 == len(s1):
                        return True
                else:
                    characters[s2[left]] -= 1
                    left += 1
                    right -= 1
            else:
                left = -1
                characters = {}
            right += 1

        return False


        