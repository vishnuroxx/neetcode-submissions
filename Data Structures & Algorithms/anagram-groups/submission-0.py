class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def checkAnagram(s : str, t : str, hsh : dict) -> bool:
            hsh_copy = hsh.copy()
            if len(s) < len(t):
                return False
            else:
                for ch in s: 
                    if hsh_copy.get(ch) == None or hsh_copy.get(ch) == 0:
                        return False
                    else: 
                        hsh_copy[ch] -= 1
                return True

        def buildHash(s : str) -> dict:
            hsh = {}
            for ch in s: 
                if hsh.get(ch) == None:
                    hsh[ch] = 1
                else:
                    hsh[ch] += 1
            return hsh

        hashes = {}
        hashtoString = {}

        for s in strs: 
            is_added = False
            if len(hashes) > 0:
                for key, hsh in hashes.items():
                    if checkAnagram(s, key, hsh):
                        hashtoString[key].append(s)
                        is_added = True

            if not is_added:
                hashes[s] = buildHash(s)
                hashtoString[s] = [s]

        result = []
        for key, items in hashtoString.items():
            result.append(items)
        

        return result
