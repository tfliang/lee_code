"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        ans = ''
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        s = 0
        while True:
            if p1 < 0 and p2 < 0 and s == 0:
                break
            if p1 < 0:
                a1 = 0
            else:
                a1 = int(num1[p1])
            if p2 < 0:
                a2 = 0
            else:
                a2 = int(num2[p2])

            s = a1 + a2 + s
            ans = str(s % 10) + ans

            if s >= 10:
                s = 1
            else:
                s = 0
            p1 -= 1
            p2 -= 1
        return ans

    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        ans = []
        k = [int(i) for i in str(K)]
        pa = len(A) - 1
        pk = len(k) - 1
        s = 0
        while(pa >= 0 or pk >= 0 or s > 0):
            tmp_a = A[pa] if pa >= 0 else 0
            tmp_k = k[pk] if pk >= 0 else 0
            s = s + tmp_a + tmp_k
            ans.insert(0, s % 10)
            s = 1 if s > 9 else 0
            pa -= 1
            pk -= 1
        return ans





if __name__ == '__main__':
    s = Solution()
    n1 = [1, 2, 0, 0]
    n2 = 34
    print(s.addToArrayForm(n1, n2))