# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rs = ListNode(0)
        p1 = l1
        p2 = l2
        v_up = 0
        prs = rs
        while(p1 or p2 or v_up):
            p = ListNode(0)
            v_sum = (p1.val if p1 else 0) + (p2.val if p2 else 0) + v_up
            if v_sum < 10:
                p.val = v_sum
                v_up = 0
                print('v', p.val)
            else:
                v_up = 1
                p.val = v_sum - 10
                print('v', p.val)
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            prs.next = p
            prs = p
        p = rs.next
        while p:
            print(p.val)
            p = p.next
        return rs.next


if __name__ == '__main__':
    s = Solution()
    a = ListNode(9)
    a.next = ListNode(3)
    a.next.next = ListNode(5)
    b = ListNode(3)
    b.next = ListNode(9)
    s.addTwoNumbers(a, b)