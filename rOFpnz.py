# =========================== Ratios OF Positive Negative and Zero =========================
# arr = [ 1, 1, 0, -1, -1 ]
# There are n = 5  elements, two positive, two negative and one zero. Their ratios are
# 2/5 = 0.400000 and 2/5 = 0.400000 and 1/5 = 0.200000
# =============================== HackerRankProblem ========================================
#Saikt
# Saikat2
import math
import os
import random
import re
import sys
def plusMinus(arr):
    # Write your code here
    n = len(arr)
    positive = 0
    negetive = 0
    zero = 0
    for i in range(n):
        if(arr[i]>0):
            positive = positive + 1
        elif(arr[i]<0):
            negetive = negetive + 1
        elif(arr[i] == 0):
            zero = zero + 1
    print(positive/n)
    print(negetive/n)
    print(zero/n)
            
# if __name__ == '__main__':''''''''''''''''
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))
arr = [1, 1, 0, -1, -1]
plusMinus(arr)


# change second time
