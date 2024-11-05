class PrefixSum:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)
            
    def range_sum(self, left, right):
        prefix_right = self.prefix[right]
        prefix_left = self.prefix[left - 1] if left > 0 else 0
        return prefix_right - prefix_left

def main():
    nums = [2, -1, 3, -3, 4]
    prefix = PrefixSum(nums)
    print(prefix.range_sum(1, 3))

if __name__ == "__main__":
    main()