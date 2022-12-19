N = int(input("Enter the multiplier:"))
A = int(input("Enter upto What digit do you want:"))
for i in range(0,A+1):
    if(i%N==0):
        print(i)
