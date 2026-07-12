from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            # Start of a sequence
            if (n - 1) not in numset:
                length = 1

                while (n + length) in numset:
                    length += 1

                longest = max(longest, length)

        return longest


# Driver code
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums = [100, 4, 200, 1, 3, 2]
    print("Input:", nums)
    print("Longest Consecutive Length:", sol.longestConsecutive(nums))

    # Example 2
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print("\nInput:", nums)
    print("Longest Consecutive Length:", sol.longestConsecutive(nums))

   