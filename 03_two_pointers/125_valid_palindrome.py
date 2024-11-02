class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        L = 0
        R = len(s) - 1
        
        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1
                
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
            
        return True
        
def main():
    sol = Solution()
    
    s = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s))
    
    s = "race a car"
    print(sol.isPalindrome(s))
    
    s = " "
    print(sol.isPalindrome(s))
    
if __name__ == "__main__":
    main()