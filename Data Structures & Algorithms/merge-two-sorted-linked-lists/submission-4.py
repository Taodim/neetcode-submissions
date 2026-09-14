# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        curr1 = list1
        curr2 = list2
        result = ListNode()
        tail = result

        while curr1 or curr2:
            if not curr1:
                tail.next = curr2
                return result.next
            elif not curr2:
                tail.next = curr1
                return result.next
            else:
                if curr1.val <= curr2.val:
                    tail.next = curr1
                    curr1 = curr1.next
                else:
                    tail.next = curr2
                    curr2 = curr2.next
            tail = tail.next
        return result.next

            