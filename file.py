f =open("Mydata.txt","r")

print(f.readline())
f1 = open("data.txt","w")
f1.write("Hello World")
f1.write(f.read())
# print(f.read())
f1.close()
f.close()