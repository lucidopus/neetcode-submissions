class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Returns the indices (1-indexed) of the integers that add up to the target.

        Args:
            numbers: list[int] = The input numbers
            target: int = The target

        Returns:
            sum_indices: list[int] = The indices (1-indexed) of the numbers adding up to the target

        Complexity:
            Time: O(n)
            Space: 

        """

        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]







