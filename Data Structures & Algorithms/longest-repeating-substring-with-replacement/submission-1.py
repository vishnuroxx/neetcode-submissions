class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0 
        left = 0 
        target_count = 0
        hash = {}
        for right, ch in enumerate(s):
            hash[ch] = hash.get(ch, 0) + 1
            target_count = max(target_count, hash[ch])

            if (right - left + 1) - target_count > k:
                hash[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result

        
        