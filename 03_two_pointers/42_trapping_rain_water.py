from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        L, R = 0, len(height) - 1
        max_L, max_R = height[L], height[R]
        total = 0
        
        while L < R:
            if max_L < max_R:
                L += 1
                vol = max_L - height[L]
                max_L = max(max_L, height[L])
                total += vol if vol >= 0 else 0 
            else:
                R -= 1
                vol = max_R - height[R]
                max_R = max(max_R, height[R])
                total += vol if vol >= 0 else 0
        
        return total
        
def main():
    sol = Solution()
    
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap(height))
    
    height = [4,2,0,3,2,5]
    print(sol.trap(height))
    
if __name__ == "__main__":
    main()