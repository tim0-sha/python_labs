m=int(input("Минуты: "))
m = m % 1440 
print(f"{m//60}:{m%60:02d}")