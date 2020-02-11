import sys
import os
from collections import deque

print("input 2 numbers")
int_1 = int(input())
int_2 = int(input())
bin_str_1 = bin(int_1)
bin_str_2 = bin(int_2)

bin_str_1 = bin_str_1.lstrip('0b')
bin_str_2 = bin_str_2.lstrip('0b')

if len(bin_str_1) != len(bin_str_2):
    print("binary strings should be of same length")

l = len(bin_str_1)

digit = deque()

carry = 0

i = l -1

print(int(str(bin_str_1)))
print(int(str(bin_str_2)))
while(i >= 0 ):
    
    div = int(bin_str_1[i]) + int(bin_str_2[i]) + carry
    dig = div//2
    rem = div%2
    carry = dig
    digit.appendleft(rem)
    i = i-1
  
digit.appendleft(carry)


li = [str(x) for x in digit]
print(li)
print(str( int(''.join(li),2) ) )

