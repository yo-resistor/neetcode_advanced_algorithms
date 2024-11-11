class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum_my(self, head: ListNode) -> int:
        sums = []
        fast, slow = head, head
        
        while fast and fast.next:
            sums.append(slow.val)
            fast = fast.next.next
            slow = slow.next
            
        idx = -1
        while slow:
            sums[idx] += slow.val
            slow = slow.next
            idx -= 1
        
        return max(sums)
    
    def pairSum(self, head: ListNode) -> int:
        slow, fast = head, head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        result = slow.val + prev.val
        while slow and prev:
            result = max(result, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        
        return result

def main():
    sol = Solution()
    
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    print(sol.pairSum(head))
    
    head = ListNode(5)
    head.next = ListNode(4)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(sol.pairSum(head))
    
    head = ListNode(1)
    head.next = ListNode(100000)
    print(sol.pairSum(head))

if __name__ == "__main__":
    main()