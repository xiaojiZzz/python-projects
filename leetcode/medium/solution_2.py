"""
两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
提示：
每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
"""
from typing import Optional

from .listnode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        flag = 0
        while l1 or l2 or flag:
            if l1:
                flag += l1.val
                l1 = l1.next
            if l2:
                flag += l2.val
                l2 = l2.next
            cur.next = ListNode(flag % 10)
            cur = cur.next
            flag //= 10
        return dummy.next


"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def anNode(node1: Optional[ListNode], node2: Optional[ListNode], flag: int) -> Optional[ListNode]:
            if node1 or node2:
                sm = (node1.val if node1 else 0) + (node2.val if node2 else 0) + flag
                return ListNode(sm % 10, anNode(node1.next if node1 else None, node2.next if node2 else None, sm // 10))
            elif flag:
                return ListNode(1)
            else:
                return None

        return anNode(l1, l2, 0)

// 第二种递归写法，直接在参数中加入 flag 并设置为默认值 0
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], flag=0) -> Optional[ListNode]:
        if l1 or l2:
            sm = (l1.val if l1 else 0) + (l2.val if l2 else 0) + flag
            return ListNode(sm % 10, self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None, sm // 10))
        elif flag:
            return ListNode(1)
        else:
            return None
"""
