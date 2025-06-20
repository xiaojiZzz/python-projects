"""
排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：
输入：head = []
输出：[]
提示：
链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105

进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
"""
from typing import Optional

from listnode import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(fast)
        dummy = cur = ListNode()
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left if left else right
        return dummy.next


"""
# 另一种写法
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
            dummy = cur = ListNode()
            while left and right:
                if left.val <= right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next
            cur.next = left if left else right
            return dummy.next

        def sort(head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
            if head is None:
                return head
            if head.next is tail:
                head.next = None
                return head
            fast = slow = head
            while fast is not tail and fast.next is not tail:
                fast = fast.next.next
                slow = slow.next
            left = sort(head, slow)
            right = sort(slow, tail)
            return merge(left, right)

        return sort(head, None)
"""

"""
class Solution:
    # 获取链表长度
    def getListLength(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    # 分割链表
    # 如果链表长度 <= size，不做任何操作，返回空节点
    # 如果链表长度 > size，把链表的前 size 个节点分割出来（断开连接），并返回剩余链表的头节点
    def splitList(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        # 先找到 next_head 的前一个节点
        cur = head
        for _ in range(size - 1):
            if cur is None:
                break
            cur = cur.next

        # 如果链表长度 <= size
        if cur is None or cur.next is None:
            return None  # 不做任何操作，返回空节点

        next_head = cur.next
        cur.next = None  # 断开 next_head 的前一个节点和 next_head 的连接
        return next_head

    # 21. 合并两个有序链表（双指针）
    # 返回合并后的链表的头节点和尾节点
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 把 list1 加到新链表中
                list1 = list1.next
            else:  # 注：相等的情况加哪个节点都是可以的
                cur.next = list2  # 把 list2 加到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2  # 拼接剩余链表
        while cur.next:
            cur = cur.next
        # 循环结束后，cur 是合并后的链表的尾节点
        return dummy.next, cur

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.getListLength(head)  # 获取链表长度
        dummy = ListNode(next=head)  # 用哨兵节点简化代码逻辑
        step = 1  # 步长（参与合并的链表长度）
        while step < length:
            new_list_tail = dummy  # 新链表的末尾
            cur = dummy.next  # 每轮循环的起始节点
            while cur:
                # 从 cur 开始，分割出两段长为 step 的链表，头节点分别为 head1 和 head2
                head1 = cur
                head2 = self.splitList(head1, step)
                cur = self.splitList(head2, step)  # 下一轮循环的起始节点
                # 合并两段长为 step 的链表
                head, tail = self.mergeTwoLists(head1, head2)
                # 合并后的头节点 head，插到 new_list_tail 的后面
                new_list_tail.next = head
                new_list_tail = tail  # tail 现在是新链表的末尾
            step *= 2
        return dummy.next
"""
