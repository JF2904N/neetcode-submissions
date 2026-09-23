class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberset = set(nums)
        longest = 0

        for num in numberset:
            if (num - 1) not in numberset:
                length = 1
                while (num + length) in numberset:
                    length += 1
                longest = max(length, longest)
        return longest