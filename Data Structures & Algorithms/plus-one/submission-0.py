class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 0

        for i in range(len(digits)):
            digit = digits[i]
            if i == 0:
                new_digit = digit + 1
            
            else:
                new_digit = digit + carry
                carry = 0
            
            if new_digit >= 10:
                    carry = 1
                    new_digit = new_digit - 10

            digits[i] = new_digit

        if carry == 1:
            digits.append(carry)
            
        digits.reverse()
        return digits
            
