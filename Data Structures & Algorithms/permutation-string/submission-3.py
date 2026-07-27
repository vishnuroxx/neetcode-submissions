class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash = {}
        for ch in s1:
            hash[ch] = hash.get(ch, 0) + 1

        character = {}
        left, right= 0, 0
        while right < len(s2):
            # consume letter
            if hash.get(s2[right]):
                if hash.get(s2[right]) >= character.get(s2[right], 0) + 1:
                    # consume 
                    character[s2[right]] = character.get(s2[right], 0) + 1
                    if right - left + 1 == len(s1):
                        return True
                else:
                    character[s2[left]] -= 1
                    left += 1
                    continue 
            else:
                # reset
                left = right + 1
                character = {}   

            right += 1
        
        return False 


        