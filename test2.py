# Asked by Facebook
# Make a program that returns the maximum product of three integers in the array.


arr = [-10, -11, 5, 2, 20, -15, -3, 20, -10]
print(arr)

negatives = []

#######Functions#################
def threeMax(arg):
    arg.sort(reverse=True)
    for i in range(len(arg)):
        return arg[i], arg[i+1], arg[i+2]

def twoMaxNeg(arg):
    arg.sort()
    for i in range(len(arg)):
        if len(arg) >= 2:
            return arg[i]*arg[i+1]
        elif len(arg) < 2:
            return 1

##############################################

# PUTTING NEGATIVES IN DIFFERENT ARRAY

for i in range(len(arr)):
    if arr[i] < 0:
        negatives.append(arr[i])

print(negatives)

# CHECK IF THERE ODD OR EVEN AMOUNT OF NEGATIVES AND NEGATIVES ARE MORE THAN 1
print(len(negatives))

if len(negatives) > 1:
    if list(threeMax(arr))[0]*list(threeMax(arr))[1] > (twoMaxNeg(arr)):
        print(list(threeMax(arr))[0]*list(threeMax(arr))[1])
    else:
        print((twoMaxNeg(arr)))

#Just to check
print(list(threeMax(arr))[0]*list(threeMax(arr))[1])
print((twoMaxNeg(arr)))
