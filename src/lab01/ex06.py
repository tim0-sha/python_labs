n=int(input("in_1: "))
ochno=0;zaochno=0
for i in range(n):
    s=input(f"in_{i+2}: ").split()
    if s[-1]=="True":
        ochno+=1
    else: zaochno+=1
print("out: ",ochno,zaochno)
