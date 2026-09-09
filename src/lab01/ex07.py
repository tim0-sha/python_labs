line=input()
word=""
flag=0
indexx_1=0;indexx_2=0;indexx_0=0
for i in range(len(line)):
    if flag==0:
        if "A" <= line[i] <= "Z": 
            word += line[i]
            indexx_1 = i
            flag = 1
    elif flag == 1:
        if "0" <= line[i] <= "9":
            word += line[i+1]
            indexx_2 = i+1
            indexx_0= i+1
            flag = 2
    else:
        if i - indexx_0 == indexx_2 - indexx_1:
            word += line[i]
            indexx_0 = i
print(word)

