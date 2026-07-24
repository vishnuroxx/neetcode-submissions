class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Linear sweep -> check end element at index with start val of newInterval 3 6 8 9 11 10
        # Check end index with start index 
        #          |-----| |------| |-|
    #     |-----|
        # Stack = [] newInterveal
        # Stacl = []
        result = []

        for interval in intervals: 
            # check if theres a collision
            if (interval[1] >= newInterval[0] and interval[1] <= newInterval[1]) \
                or (newInterval[1] >= interval[0] and newInterval[1] <= interval[1]):
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
            else:
                result.append(interval)
        
        curr = 0 
        while curr < len(result) and result[curr][0] < newInterval[1]:
            curr += 1

        result.insert(curr, newInterval)
        return result