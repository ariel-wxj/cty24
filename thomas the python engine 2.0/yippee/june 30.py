"""
numbers=[1,2,3,4,5,6,7,8]
numbers2=[]


numbers.reverse()
print(numbers)

for i in numbers:
    numbers2.insert(0,i)


print(numbers2)
"""

"""
a=[1,"c",1]
b=[0,"c",0]
c=[0,"c",1]

for i in range(1):
    if a[0] == 1 and a[2] == 1:
        print("you won")
    elif a[0] == 1 and a[2] == 0 or a[0] == 0 and a[2] == 1:
        print("youre close to winning")

    else:
        print("you lost")

    if b[0] == 1 and b[2] == 1:
        print("you won")
    elif b[0] == 1 and b[2] == 0 or b[0] == 0 and b[2] == 1:
        print("youre close to winning")
    else:
        print("you lost")

    if c[0] == 1 and c[2] == 1:
        print("you won")
    elif c[0] == 1 and c[2] == 0 or c[0] == 0 and c[2] == 1:
        print("youre close to winning")
    else:
        print("you lost")

"""

number = int(input("enter an number:"))

f = 1

for i in range(number, 0, -1):
    f *= i



count=0

while(f>0):
    count=count+1
    f=f//10


res = (format (f, ",d"))


print(f)
print(str(res))
