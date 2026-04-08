from math import sqrt
mylist =[]
tot = 0
n=int(input('Enter the Number of items:'))
print('Enter ', n,' the items:')
for i in range(n):
    item  = int (input())
    mylist +=[item]#append()
    tot += item
mean = tot / n
tot = 0
for items in mylist:
    tot += (item - mean) * (item - mean)
var = tot / n
std = sqrt(var)
print("Mean =", mean)
print("Variance =", var)
print("Standard Deviation =",std)        