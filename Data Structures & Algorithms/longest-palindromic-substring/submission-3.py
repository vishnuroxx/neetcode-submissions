class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        is_palindrome = [[True for i in range(len(s))] for j in range(len(s))]
        max_pair = (0, 0)


        for i in range(len(s)-1,-1,-1):
            for j in range(len(s)):
                if i < j:
                    if s[i] != s[j] or i + 1 <= j - 1 and not is_palindrome[i + 1][j - 1]:
                        is_palindrome[i][j] = False 
        
        
        for i in range(len(s)):
            for j in range(len(s)):
                if i < j and is_palindrome[i][j] and j - i> max_pair[1] - max_pair[0]:
                    max_pair = (i, j)

        return s[max_pair[0] : max_pair[1] + 1]
            


        