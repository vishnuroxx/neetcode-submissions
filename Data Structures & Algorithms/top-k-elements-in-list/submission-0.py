class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for idx in range(len(nums)):
            if hash.get(nums[idx]):
                hash[nums[idx]] += 1
            else:
                hash[nums[idx]] = 1
        result = list(hash.keys())
        result.sort(key=lambda x: hash[x])
        return result[len(result)-k:]
