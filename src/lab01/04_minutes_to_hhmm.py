m=int(input("Минуты: "))
days = m // 1440 
m = m - days * 1440 
print(f"{m//60}:{m%60:02d}")