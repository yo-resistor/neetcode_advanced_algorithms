from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        window = set()
        length = 0
        
        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            
            window.add(s[R])
            length = max(length, len(window))
            
        return length
    
def main():
    sol = Solution()
    
    s = "abcdabcbb"
    print(sol.lengthOfLongestSubstring(s))
    
    s = "bbbbb"
    print(sol.lengthOfLongestSubstring(s))
    
    s = "pwwkew"
    print(sol.lengthOfLongestSubstring(s))
    
if __name__ == "__main__":
    main()