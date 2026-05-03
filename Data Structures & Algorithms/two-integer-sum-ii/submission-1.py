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
            Time:
            Space: 

        """

        seen_numbers = {}

        for i in range(len(numbers)):
            
            missing_piece = target - numbers[i]

            if missing_piece in seen_numbers:
                return [seen_numbers[missing_piece]+1, i+1]
            else:
                seen_numbers[numbers[i]] = i
        







