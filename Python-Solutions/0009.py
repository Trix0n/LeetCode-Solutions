"""
PALINDROME NUMBER

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

    -231 <= x <= 231 - 1

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_x = 0
        y = x

        if x < 0:
            return False
        else:
            while y > 0:
                remainder = y % 10
                reverse_x = (reverse_x * 10) + remainder
                y = y // 10
        
        if reverse_x == x:
            return True
        else:
            return False
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        y = x
        num = 0
        while y > 0:
            z = y % 10
            num = (num * 10) + z
            y = y//10

        if num == x:
            return True
        else:
            return False