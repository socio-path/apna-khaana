#DIET PLAN
def getdate():
    import datetime
    return datetime.datetime.now()

print("d, s, m")
a = int(input())
print ("put, retrieve")
b = int(input())

if a == 1 and b == 1:
     f = open("python.txt", "a")
     f.write(str(getdate()) + " : " + input() + "\n")

     f.close()
elif a==2 and b==1:
     f = open("python1.txt", "a")
     f.write(str(getdate()) + " : " + input() + "\n")
     print("Success")
     f.close()
elif a==3 and b==1:
     f = open("python2.txt", "a")
     f.write(str(getdate()) + " : " + input() + "\n")
     print("Success")
     f.close()
elif a==1 and b==2:
     f = open("python.txt", "rt")
     a1 = f.read()
     print(a1)
     f.close()
elif a==2 and b==2:
     f = open("python1.txt")
     a2 = f.read()
     print(a2)
     f.close()
elif a==3 and b == 2:
     f = open("python2.txt")
     a3 = f.read()
     print(a3)
     f.close()

