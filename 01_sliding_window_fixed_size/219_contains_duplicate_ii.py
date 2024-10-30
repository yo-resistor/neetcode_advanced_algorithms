from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        L = 0
        window = set()
        window.add(nums[L])
        
        for R in range(1, len(nums)):
            # if R is out of the window, remove L pointer's value
            # and move L pointer to the right by 1
            if R - L >= k + 1:
                window.remove(nums[L])
                L += 1
                
            # if R pointer's value is in hash set, return True
            if nums[R] in window:
                return True
            
            # default action: add R pointer's value to the hash map
            window.add(nums[R])
        
        return False
    
def main():
    sol = Solution()
    
    nums = [1,2,3,1]
    k = 3
    print(sol.containsNearbyDuplicate(nums, k))
    
    nums = [1,0,1,1]
    k = 1
    print(sol.containsNearbyDuplicate(nums, k))
    
    nums = [1,2,3,1,2,3]
    k = 2
    print(sol.containsNearbyDuplicate(nums, k))
    
if __name__ == "__main__":
    main()