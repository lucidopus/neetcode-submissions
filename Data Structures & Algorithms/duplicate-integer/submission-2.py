class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Returns a boolean for an array having a duplicate or not.

        Complexity:
            Time: 
            Space: 
        """

        nums_set = set(nums)

        return not (len(nums_set) == len(nums))

