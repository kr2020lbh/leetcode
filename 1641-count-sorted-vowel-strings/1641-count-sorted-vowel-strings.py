class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = [ [1]*5 for _ in range(n)]
        for i in range(1,n):
            for j in range(1,5):
                vowels[i][j] = vowels[i-1][j] + vowels[i][j-1]
        return sum(vowels[n-1])
        
        