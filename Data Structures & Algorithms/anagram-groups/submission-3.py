class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sortStrs = [''.join(sorted(list(s))) for s in strs] #klogk 
    
        hash = {}
        curr = 0
        for idx in range(len(strs)): # O(nk)
            ptr = hash.get(sortStrs[idx])
            if ptr != None:
                result[ptr].append(strs[idx])
            else:
                result.append([strs[idx]])
                hash[sortStrs[idx]] = curr
                curr += 1
                
        return result