class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash = {}
        for ch in s1:
            hash[ch] = hash.get(ch, 0) + 1

        for left in range(len(s2)-len(s1) + 1):
            print(left)
            characters = {}
            for i in range(len(s1)):
                print(s2[left], s2[left + i])
                if hash.get(s2[left + i]) and hash.get(s2[left + i]) >= characters.get(s2[left + i], 0) + 1:
                    characters[s2[left+i]] = characters.get(s2[left + i], 0) + 1
                    if i == len(s1) - 1:
                        return True
                else:
                    break

        return False


        