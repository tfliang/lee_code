from typing import List


class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        len_p = len(prices)
        rs = 0
        for i in range(len_p - 1):
            for pj in prices[i+1:]:
                pi = prices[i]
                d = pj - pi
                rs = d if d>rs else rs
        print(rs)
        return rs

    def maxProfit(self, prices: List[int]) -> int:
        rs = 0
        p_min = float('inf')
        for p in prices:
            p_min = min(p_min, p)
            rs = max(rs, p - p_min)
        return rs


if __name__ == '__main__':
    s = Solution()
    import numpy as np
    a = [np.random.randint(1, 19) for i in range(10)]
    s.maxProfit(a)
