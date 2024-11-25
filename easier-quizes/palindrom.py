# given an integer, return True if it is a palindrome, False otherwise


# example: 121 -> True explanation: 121 == 121
# example: 123 -> False explanation: 123 != 321
# example: 1221 -> True explanation: 1221 == 1221


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]
 
# test cases
print(is_palindrome(121)) # True
print(is_palindrome(123)) # False
  
    