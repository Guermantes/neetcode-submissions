# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted = ListNode()
        cur = sorted
        while True:
            argmin = -1
            min = 1001
            for i in range(len(lists)):
                if lists[i] != None and lists[i].val < min:
                    argmin = i
                    min = lists[i].val

            if argmin == -1:
                break

            cur.next = lists[argmin]
            lists[argmin] = lists[argmin].next
            cur = cur.next

        return sorted.next