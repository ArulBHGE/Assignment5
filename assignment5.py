# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:55:38 2022

@author: 105042833
"""

class Solution(object):
   def Pow(self, x, n):
      power = abs(n)
      res = 1.0
      while power:
         if power & 1:
            res*=x
         x*=x
         power>>=1
      if n<0:
         return 1/res
      return res
ob1 = Solution()
num=int(input("Enter the number:"))
pp=int(input("Enter the power:"))
print(ob1.Pow(num, pp))