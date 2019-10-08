"""
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1-bit-and-2-bit-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        start = 0
        len_bits = len(bits)
        while True:
            if start == len_bits - 1:
                return True
            elif start >= len_bits:
                return False
            if bits[start] == 1:
                start += 2
            else:
                start += 1


if __name__ == '__main__':
    s = Solution()
    b = [0, 1, 1, 0]
    print(s.isOneBitCharacter(bits=b))

