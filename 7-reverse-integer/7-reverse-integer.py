class Solution:
    def reverse(self, x: int) -> int:
        lowLimit = -2**31
        highLimit = 2**31-1
        signFlag = 1
        res = []
        if x < 0:
            signFlag = 0
        zeroFlag = 0
        if not signFlag:
            x = -x
        while x:
            mod = x%10
            x//=10
            if zeroFlag == 0 and mod:
                zeroFlag = 1
            if zeroFlag:
                res.append(str(mod))
        answer = 0
        if res:
            answer = int(''.join(res))
            if not signFlag:
                answer = -answer
            if not (lowLimit <= answer <= highLimit):
                answer = 0
        return answer