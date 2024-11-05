from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        prefix_right = self.prefix[right]
        prefix_left = self.prefix[left - 1] if left > 0 else 0
        return prefix_right - prefix_left

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

def main():
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)
    print(num_array.sumRange(0, 2))
    print(num_array.sumRange(2, 5))
    print(num_array.sumRange(0, 5))

if __name__ == "__main__":
    main()