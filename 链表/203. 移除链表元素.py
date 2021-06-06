# _*_coding:utf-8 _*_
# @Time    : 2021/6/5 16:38
# @Author  : Guo 
# @File    : 203. 移除链表元素.py
# @Desc    :https://leetcode-cn.com/problems/remove-linked-list-elements/
"""
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], val = 1
输出：[]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        pre = ListNode()
        pre.next = head
        cur = pre
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return pre.next