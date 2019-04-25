from typing import List


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        s_nums = sorted(nums)
        print(s_nums)
        len_nums = len(nums)

        min_d = float("inf")
        for l, vl in enumerate(s_nums[:-2]):
            m = l + 1
            vm = s_nums[m]
            r = len_nums - 1
            vr = s_nums[r]

            tmp_min = vl + vm * 2 - target
            tmp_max = vl + vr * 2 - target


            if tmp_max * tmp_min > 0 and abs(min_d) < min(abs(tmp_min), abs(tmp_max)):
                break

            while(m < r):
                d = vl + s_nums[m] + s_nums[r] - target
                print('{}, {}, {}: {}, {}'.format(vl, vm, vr, d, d+target))
                if abs(d) < abs(min_d):
                    min_d = d
                if d == 0:
                    return d + target
                elif d > 0:
                    r -= 1
                elif d < 0:
                    m += 1
                print('{}'.format(min_d + target))
        return min_d + target



if __name__ == '__main__':
    import numpy as np
    s = Solution()
    np.random.seed(2)
    nums = [np.random.randint(-9, 12) for i in range(10)]
    nums = [-1, 2, 1, -4]
    nums = [-3,-2,-5,3,-4]
    rs = s.threeSumClosest(nums, -1)
    print(rs)
