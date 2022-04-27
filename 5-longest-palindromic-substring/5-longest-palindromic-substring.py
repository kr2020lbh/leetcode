class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        
        dp = [[0]*slen for _ in range(slen)]
        
        for i in range(slen):
            dp[i][i] = 1
                
        for i in range(slen-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
        
        for i in range(3,slen+1):
            for j in range(slen-i+1):
                s_idx,e_idx = j,j+i-1
                if s[s_idx] == s[e_idx] and dp[s_idx+1][e_idx-1]:
                    dp[s_idx][e_idx] = 1
                    
        maxlen = 0
        answer = 0
        
        for i in range(slen):
            for j in range(slen):
                if dp[i][j] and maxlen < j-i+1:
                    answer = s[i:j+1]
                    maxlen = j-i+1
                    
        return answer 
                    