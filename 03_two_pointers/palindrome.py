def is_palindrome(word) -> bool:
    L = 0
    R = len(word) - 1
    
    while L < R:
        if word[L] != word[R]:
            return False
        L += 1
        R -= 1
    return True

def main():
    word = [1, 2, 7, 7, 2, 1]
    print(is_palindrome(word))
    
    word = [1, 2, 3, 4, 3, 2, 1]
    print(is_palindrome(word))
    
    word = [1, 2, 3, 3, 1]
    print(is_palindrome(word))
    
if __name__ == "__main__":
    main()