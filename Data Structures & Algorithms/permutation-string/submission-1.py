class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash = {}
        for ch in s1:
            hash[ch] = hash.get(ch, 0) + 1

        character = {}
        left, right= 0, 0
        while right < len(s2):
            # consume letter
            char = s2[right]
            character[char] = character.get(char, 0) + 1
            if hash.get(char, 0):
                if character[char] <= hash[char]:
                    if right - left + 1 == len(s1):
                        return True
                    else:
                        right += 1
                else:
                    character[char] -= 1
                    character[s2[left]] -= 1
                    left += 1
            else:
                left = right + 1
                character = {}
                right += 1
        
        return False 


        