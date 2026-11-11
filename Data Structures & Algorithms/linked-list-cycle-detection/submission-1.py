# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        setNodes = set()
        curr = head
        while curr:
            if curr in setNodes:
                return True
            setNodes.add(curr)
            curr = curr.next
        return False
        