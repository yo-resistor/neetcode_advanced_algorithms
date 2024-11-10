class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        # if no cycle, return NULL
        if not fast or not fast.next:
            return None
        
        # if cycle, return the cycle starting node
        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next
        return slow2

def main():
    sol = Solution()
    
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next.next
    
    print(sol.detectCycle(head))

if __name__ == "__main__":
    main()