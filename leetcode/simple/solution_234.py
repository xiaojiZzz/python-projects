"""
回文链表
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
示例 1：
输入：head = [1,2,2,1]
输出：true
示例 2：
输入：head = [1,2]
输出：false
提示：
链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9

进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
from typing import Optional

from .listnode import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next
        slow.next = None
        slow = tmp

        def reverseList(h: Optional[ListNode]) -> Optional[ListNode]:
            pre = None
            cur = h
            while cur is not None:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        p = reverseList(slow)
        while p is not None:
            if head.val != p.val:
                return False
            head, p = head.next, p.next
        return True


"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        st = []
        while slow is not None:
            st.append(slow)
            slow = slow.next
        while st:
            if head.val != st.pop().val:
                return False
            head = head.next
        return True
"""

"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = head

        def check(node: Optional[ListNode]):
            nonlocal p
            if node is not None:
                if not check(node.next):
                    return False
                if p.val != node.val:
                    return False
                p = p.next
            return True

        return check(head)
"""
