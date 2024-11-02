def target_sum(nums, target):
    L = 0
    R = len(nums) - 1
    
    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1
        elif nums[L] + nums[R] < target:
            L += 1
        else:
            return [L, R]
    
def main():
    nums = [-1, 2, 3, 4, 8, 9]
    print(target_sum(nums, 5))

    nums = [-1, 2, 3, 4, 7, 9]
    print(target_sum(nums, 7))
    
if __name__ == "__main__":
    main()