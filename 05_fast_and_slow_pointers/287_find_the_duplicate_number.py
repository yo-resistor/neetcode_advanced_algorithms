class Solution(object):
    def findDuplicate(self, nums) -> int:
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2
    
    def findDuplicate_brute_force(self, nums) -> int:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]

def main():
    sol = Solution()
    
    nums = [1,3,4,2,2]
    print(sol.findDuplicate(nums))
    
    nums = [3,1,3,4,2]
    print(sol.findDuplicate(nums))
    
    nums = [3,3,3,3,3]
    print(sol.findDuplicate(nums))

if __name__ == "__main__":
    main()