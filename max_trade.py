"""
A:
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

B:
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxProfit_On2(self, prices: List[int]) -> int:
        len_p = len(prices)
        rs = 0
        for i in range(len_p - 1):
            for pj in prices[i+1:]:
                pi = prices[i]
                d = pj - pi
                rs = d if d>rs else rs
        print(rs)
        return rs

    def maxProfit_A(self, prices: List[int]) -> int:
        rs = 0
        p_min = float('inf')
        for p in prices:
            p_min = min(p_min, p)
            rs = max(rs, p - p_min)
        return rs

    def maxProfit_B(self, prices: List[int]) -> int:
        s = 0
        for i in range(len(prices) - 1):
            d = prices[i + 1] - prices[i]
            if d >= 0:
                s += d
        return s


if __name__ == '__main__':
    s = Solution()
    import numpy as np
    a = [np.random.randint(1, 19) for i in range(10)]
    s.maxProfit_A(a)
