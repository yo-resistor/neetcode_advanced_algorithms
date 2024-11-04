from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        idx = 0
        ptr = 1
        
        for ptr in range(1, len(nums)):
            if nums[idx] != nums[ptr]:
                idx += 1
                nums[idx] = nums[ptr]
        
        return idx + 1
    
def main():
    sol = Solution()
    
    nums = [1, 1, 2]
    print(sol.removeDuplicates(nums))
    
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(sol.removeDuplicates(nums))
    
if __name__ == "__main__":
    main()