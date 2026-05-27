class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []
        b = []

        product = 1
        for num in nums:
            product*=num
            a.append(product)
        product=1
        for num in reversed(nums):
            product*=num
            b.append(product)
        b.reverse()
        print(a)
        print(b)
        output = []
        for index in range(len(nums)):
            product = 1
            if index-1>=0:
                product*=a[index-1]

            if index+1<len(nums):
                product*=b[index+1]
            output.append(product)


        return output
        