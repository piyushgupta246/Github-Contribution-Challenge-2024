'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

'''

#Given code has used type conversion for solution come up with a code that not uses type conversion.
#You need to correct complete function body.
#Do not change class name and method name.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        
        result = num1 + num2

        result_binary = bin(result)
        
        return str(result_binary)[2:]
    
obj=Solution()
a = "1010"
b = "1011"
print(obj.addBinary(a,b))
