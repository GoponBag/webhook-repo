# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example
# arr = [1,2,3,4,3,2,1]
# The unique element is 4 .
# Print Unique element 565
# ===========================Hacker Rank Day 1 one Problem======================================
# iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
a = [1, 2, 3, 4, 3, 2, 1, 5, 8, 7, 9, 10, 7]


def lonelyinteger(a):
    # Write your code here
    l = len(a)
    arr = []
    for i in range(l):
        if (a.count(a[i]) == 1):
            arr.append(a[i])
    return arr

print (lonelyinteger(a))
