class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Linear sweep -> check end element at index with start val of newInterval 3 6 8 9 11 10
        # Check end index with start index 
        #          |-----| |------| |-|
    #     |-----|
        # Stack = [] newInterveal
        # Stacl = []
        result = []
        curr = 0
        merged = False 
        added = False 
        while curr < len(intervals): 
            while curr < len(intervals) and ((intervals[curr][1] >= newInterval[0] and intervals[curr][1] <= newInterval[1]) \
                or (newInterval[1] >= intervals[curr][0] and newInterval[1] <= intervals[curr][1])):
                newInterval = [min(newInterval[0], intervals[curr][0]), max(newInterval[1], intervals[curr][1])]
                curr += 1 
                merged = True

            if merged and not added:
                result.append(newInterval)
                added = True
            else:
                if not added and newInterval[1] < intervals[curr][0]:
                    result.append(newInterval)
                    added = True
                result.append(intervals[curr])
                curr += 1
        
        if not added:
            result.append(newInterval)
               

        return result