# Asked by google

#Given a array of numbers representing the stock prices of a company in chronological order,
#write a function that calculates the maximum profit you could have made from buying and selling that stock once.
#You must buy before you can sell it.
import math

stock = [7,13,6,5,99,28,1,44,33,99]

#Go through the array
#find the largest number in array
largestNumber = max(stock)
print(largestNumber)

test = stock.index(largestNumber)
print(test)
#find the smallest number before the largest number
indexOfLargestNumber = stock.index(largestNumber)
slicedArray = stock[0:indexOfLargestNumber+1]
smallestNumber1 = min(slicedArray)
print(smallestNumber1)
#get the difference of them
difference1 = largestNumber-smallestNumber1
#find the smallest number
smallestNumber = min(stock)
print(smallestNumber)
#check if the smallest number is before the larges number
if stock.index(largestNumber) > stock.index(smallestNumber):
    flag = "green"
    print(flag)
else:
    flag = "red"
    print(flag)
#if not then find the largest number after the smallest number
length = len(stock)
slicedArray1 = stock[stock.index(smallestNumber):len(stock)+1]
largestNumber1 = max(slicedArray1)
print(largestNumber1)
#get the difference
difference2 = largestNumber1-smallestNumber
print(difference2)
print(difference1)
#compare with the previous difference
indexOfSmallestNumber = stock.index(smallestNumber)
indexOfSmallestNumber1 = stock.index(smallestNumber1)
if difference2 > difference1:
    print(smallestNumber)
else:
    print(smallestNumber1)
