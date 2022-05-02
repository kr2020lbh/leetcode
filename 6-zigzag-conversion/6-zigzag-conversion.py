class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            m_list = list(range(numRows-1))
            orders = m_list + [numRows-1] + m_list[::-1]
            orders.pop()        
            orders = orders*(len(s) // len(orders) + 1)
            rows = ["" for _ in range(numRows)]
            for i in range(len(s)):
                rows[orders[i]] += s[i]
            return ''.join(rows)
        