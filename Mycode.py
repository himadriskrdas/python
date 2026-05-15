arr =[1,2,3,5,10,11,13,34,199]

n = int(input("Enter the item :  "))

for i in arr:
    if i == n:
        print("{} value found in {} index".format(n,i))
        break
    else:
        print("{} not found i".format(n))