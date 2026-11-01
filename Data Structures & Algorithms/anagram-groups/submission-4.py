class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        result = []
        ptr = 0
        for item in strs:
            str_sorted = "".join(sorted(item))
            index = hash.get(str_sorted)
            if index != None:
                result[index].append(item)
            else:
                hash[str_sorted] = ptr
                result.append([item])
                ptr += 1
        return result