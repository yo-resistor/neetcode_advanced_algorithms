def kadanes(nums):
    # https://www.notion.so/0-Kadane-s-Algorithm-129e0c5aec4081bda0d5c9524727da9a?pvs=4
    # if the previous sum is negative, we do not add that to the current value
    # if the previous sum is positive, we add that to the current value
    # not adding the negative value is same as adding 0
    max_sum = nums[0]
    cur_sum = 0
    
    for num in nums:
        cur_sum = max(cur_sum, 0)
        cur_sum += num
        max_sum = max(cur_sum, max_sum)
    return max_sum

def main():
    nums = [4, -1, 2, -7, 3, 4]
    print(kadanes(nums))
    
if __name__ == "__main__":
    main()