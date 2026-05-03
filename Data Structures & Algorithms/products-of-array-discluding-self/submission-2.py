class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1,2,4,6] -> [48, 24, 12, 8]
        #  ^

        left_products = [] # [1, 2, 8]
        right_products = [] # [1, 2, 8]

        products = []

        running_product = 1
        
        for i in range(len(nums)):
            left_products.append(running_product)
            running_product *= nums[i]
        
        running_product = 1

        for i in range(len(nums) - 1, -1, -1):
            right_products.append(running_product)
            running_product *= nums[i]
        
        right_products = right_products[::-1]

        for i in range(len(nums)):
            products.append(left_products[i] * right_products[i])

        return products


