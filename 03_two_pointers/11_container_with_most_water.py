from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        max_vol = 0
        
        while L < R:
            vol = (R - L) * min(height[L], height[R])
            max_vol = max(max_vol, vol)
            
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        
        return max_vol
    
def main():
    sol = Solution()
    
    height = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(height))
    
    height = [1,1]
    print(sol.maxArea(height))
    
if __name__ == "__main__":
    main()