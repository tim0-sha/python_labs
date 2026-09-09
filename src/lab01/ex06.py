n=int(input())
ochno=0;zaochno=0
for i in range(n):
    s=input().split()
    if s[-1]=="True":
        ochno+=1
    else: zaochno+=1
print(ochno,zaochno)
