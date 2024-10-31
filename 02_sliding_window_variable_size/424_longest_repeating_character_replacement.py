from typing import Dict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        hash_map = dict()
        length = 0
        
        for R in range(len(s)):
            if s[R] not in hash_map:
                hash_map[s[R]] = 0
            hash_map[s[R]] += 1
            print(length, hash_map, k)
            
            while ((R - L + 1) - self.find_max_hash(hash_map)) > k:
                hash_map[s[L]] -= 1
                L += 1
                
            length = max(length, R - L + 1)
            
        return length

    def find_max_hash(self, hash_map: dict) -> int:
        max_val = 0
        for char in hash_map:
            max_val = max(max_val, hash_map[char])
        return max_val
    
def main():
    sol = Solution()
    
    s = "ABAB"
    k = 2
    print(sol.characterReplacement(s, k))
    
    s = "AABABBA"
    k = 1
    print(sol.characterReplacement(s, k))
    
if __name__ == "__main__":
    main()