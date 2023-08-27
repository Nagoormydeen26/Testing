n = 25
flag = 0
for i in range(2,n):
    if n%i==0:
        flag+=1
if flag>0:
    print(f"{n} is not a prime number.")
else:
    print(f"{n} is a prime number.")