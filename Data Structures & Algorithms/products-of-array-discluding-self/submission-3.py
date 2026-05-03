class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # left_products = [] 
        # right_products = []

        products = []

        running_product = 1

        for i in range(len(nums)):
            products.append(running_product)
            running_product *= nums[i]
        
        running_product = 1

        for i in range(len(nums) - 1, -1, -1):
            # right_products.append(running_product)
            products[i] *= running_product
            running_product *= nums[i]
        
        return products


