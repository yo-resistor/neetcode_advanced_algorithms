from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        total = 0
        length = float("inf")
        
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(length, R - L + 1)
                total -= nums[L]
                L += 1
                
        return 0 if length == float("inf") else length
        
def main():
    sol = Solution()
    
    target = 7
    nums = [2,3,1,2,4,3]
    print(sol.minSubArrayLen(target, nums))
    
    target = 4
    nums = [1,4,4]
    print(sol.minSubArrayLen(target, nums))
    
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    print(sol.minSubArrayLen(target, nums))
    
if __name__ == "__main__":
    main()