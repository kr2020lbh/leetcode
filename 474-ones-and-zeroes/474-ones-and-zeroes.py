from collections import defaultdict
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(lambda : [[0]*(n+1) for _ in range(m+1)])
        strs = [[s.count("0"),s.count("1")] for s in strs]
        for idx,(zero,one) in enumerate(strs):
            for _zero in range(m+1):
                for _one in range(n+1):
                    if _zero-zero < 0 or _one - one < 0:
                        dp[idx][_zero][_one] = dp[idx-1][_zero][_one]
                    else:
                        dp[idx][_zero][_one] = max(1 + dp[idx-1][_zero-zero][_one-one],dp[idx-1][_zero][_one])
        return dp[idx][-1][-1]
        