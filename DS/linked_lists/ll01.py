# Write a program in Python to -
# 1. Merge two singly linked lists without creating new nodes.
# 2. Find the middle element of the linked list in a single pass.
# 3. Insert a node in a linked list.
# 4. Find the sum of two numbers represented as linked lists.
# 5. Find the second number of linked lists from the last in a single pass.

from __future__ import annotations
from typing import Any, List


class Node:
    """Single linked list node."""

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None


class LinkedList:
    """Single linked list."""

    def __init__(self) -> None:
        self.head = None

    def append(self, value: Any) -> None:
        """Insert node to the end of list."""

        temp = Node(value)

        if not self.head:
            self.head = temp
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = temp

    def __len__(self) -> int:
        if not self.head:
            return 0

        length = 0
        curr = self.head
        while curr:
            curr = curr.next
            length += 1

        return length

    def insert(self, position: int, value: Any) -> None:
        """Insert node to the list."""

        if not self.head:
            self.append(value)
            return

        # Get length of linked list
        length = len(self)

        if position < 0 or position > length:
            raise ValueError

        temp = Node(value)

        # Edge case: insert at beginning
        if position == 0:
            prev = self.head
            self.head = temp
            self.head.next = prev
            return

        # Edge case: insert at end
        if position == length:
            self.append(value)
            return

        index = 0
        curr = self.head
        prev = curr
        while index < position:
            prev = curr
            curr = curr.next
            index += 1

        prev.next = temp
        temp.next = curr

    @staticmethod
    def from_array(values: List[Any]) -> LinkedList:
        """Make linked list from array of values"""
        linked_list = LinkedList()
        for value in values:
            linked_list.append(value)
        return linked_list

    @staticmethod
    def merge_lists(linked_list_a: LinkedList, linked_list_b: LinkedList) -> LinkedList:
        """Merge two linked lists into one. Destructive."""

        head_a = linked_list_a.head
        head_b = linked_list_b.head

        # Choose starting node

        curr = None

        if head_a.value <= head_b.value:
            curr = head_a
            head_a = head_a.next
        else:
            curr = head_b
            head_b = head_b.next

        ret_node = curr

        # Process nodes

        while head_a and head_b:
            if head_a.value <= head_b.value:
                curr.next = head_a
                head_a = head_a.next
            else:
                curr.next = head_b
                head_b = head_b.next
            curr = curr.next

        # Add remaining chain of nodes

        if head_a:
            curr.next = head_a
        else:
            curr.next = head_b

        ll = LinkedList()
        ll.head = ret_node
        return ll


ll_a = LinkedList.from_array([10, 20, 26, 30, 40, 50])
ll_b = LinkedList.from_array([5, 15, 15, 17, 23, 25, 35])

ll_c = LinkedList.merge_lists(ll_a, ll_b)

print(ll_a)
