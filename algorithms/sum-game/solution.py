class Solution(object):
    def checkDivisibility(self, n):
        original = n
        sum_digits = 0
        product_digits = 1

        while n > 0:
            digits = n % 10
            sum_digits = sum_digits + digits
            product_digits = product_digits*digits

            n = n//10

        sum_all = sum_digits + product_digits

        if original % sum_all == 0:
            return True
        else:
            return False
        

        