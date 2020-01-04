import os 
import sys


class Solution:

    def __init__(self):
        pass

    
    def driver(self, a:str, b:str, aIndex:int, bIndex:int)->int:

        if aIndex == -1 or bIndex == -1:
            return 0

        if a[aIndex] == b[bIndex]:
            return self.driver(a, b, aIndex-1, bIndex-1) + 1
        else:
            return (max(self.driver(a, b, aIndex-1, bIndex), self.driver(a, b, aIndex, bIndex-1)))

    def max(self, a:int, b:int)->int:
        if a > b:
            return a
        else:
            return b
