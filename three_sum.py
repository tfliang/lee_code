from typing import List
from collections import Counter


class Solution:

    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        n = Counter(nums)
        keys = list(n.keys())
        rs = []
        if n[0] >=3:
            rs.append((0, 0, 0))
        for i in range(len(keys)):
            ak, av = n.popitem()
            for bk, bv in n.items():
                ck = - ak - bk
                cv = n.get(ck, -1)
                if (ck == bk and bv > 1) or (ck == ak and av > 1) or (ck != ak and ck != bk and cv >= 1):
                    rs.append(tuple(sorted((ak, bk, ck))))
        rs = list(set(rs))
        return rs

    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        n = Counter(nums)
        rs = []
        if n[0] >=3:
            rs.append((0, 0, 0))
        keys = list(n.keys())
        for ai, a in enumerate(keys[:-1]):
            for bi, b in enumerate(keys[ai + 1:]):
                c = - a - b
                cn = n.get(c, -1)
                if cn < 0:
                    pass
                elif ((c == a or c == b) and cn > 1) or (c != a and c != b and cn >= 1):
                    tmp = tuple(sorted((a, b, c)))
                    rs.append(tmp)
        rs = list(set(rs))
        rs.sort()
        return rs


if __name__ == '__main__':
    import numpy as np
    import time
    sl = Solution()
    np.random.seed(1)
    nums = [np.random.randint(-5, 9) for i in range(20)]
    print(nums)
    tic = time.time()
    rs1 = sl.threeSum_1(nums)
    toc = time.time() - tic
    print(toc)

    tic = time.time()
    rs2 = sl.threeSum_2(nums)
    toc = time.time() - tic
    print(toc)
    print(rs1)
    print(rs2)
    print(rs1 == rs2)
