class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_num = 0
        original_num = x
        
        if x < 0:
            return False
        
        while original_num != 0:
            last_digit = original_num % 10
            reverse_num = (reverse_num * 10 ) + last_digit
            original_num = (original_num - last_digit) // 10
        
        return reverse_num == x
