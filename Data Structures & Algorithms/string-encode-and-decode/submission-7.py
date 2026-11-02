class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "*" + string
        return result

    
    def decode(self, s: str) -> List[str]:
        result = []
        ptr = 0
        while ptr < len(s):
            # find next n
            n_str = ""
            while s[ptr] != '*':
                n_str += s[ptr]
                ptr += 1
            ptr += 1
            n = int(n_str)
            if n:
                result.append(s[ptr : ptr + n])
                ptr += n
            else:
                result.append("")
        return result


