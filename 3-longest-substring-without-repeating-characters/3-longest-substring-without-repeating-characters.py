class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = []
        res = 0
        for w in s:
            if w in word:
                idx = word.index(w)
                word = word[idx+1:]
            word.append(w)
            res = max(res,len(word))
        return res
        