class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns the product of all elements except itself

        Args:
            nums: list[int] = List of numbers

        Returns:
            products: list[int] = Products of all elements except itself

        Complexity:
            Time: O(n)
            Space: O(1)

        """
        products = []

        running_product = 1

        for i in range(len(nums)):
            products.append(running_product)
            running_product *= nums[i]
        
        running_product = 1

        for i in range(len(nums) - 1, -1, -1):
            products[i] *= running_product
            running_product *= nums[i]
        
        return products


