import array

# Sometimes in the survey engine, JS with zebra datepicker isnt accepted in XMLself.
# I made a solution to do it with python internallyself.
# It limits the date picking to only from May to August,

q11 = "05.08"

flag = 0

arr = str(q11)
months = ["8","5","6","7"]
if q11 is not None:
    if arr[3] == "0":
        for i in range(4):
            if arr[4] == months[i]:
                flag = 1
        if flag == 1:
            print("success")
        else:
            print("fail")
    else:
        print("red")

print(arr[3])
