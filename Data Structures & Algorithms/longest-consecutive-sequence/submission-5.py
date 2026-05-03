class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,20,4,10,3,4,5]

        # Early exit
        if nums == []:
            return 0

        set_nums = set(nums) # {2,20,4,10,3,4,5}

        longest_sequence_length = 1

        for number in set_nums:
            streak = 0

            # First check if we are at the lowest number 

            if (number-1) in set_nums:
                continue
            
            current = number

            while current in set_nums:
                streak += 1
                current += 1
            
            longest_sequence_length = max(longest_sequence_length, streak)

        return longest_sequence_length




