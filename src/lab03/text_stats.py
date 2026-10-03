from src.lib.text import normalize, tokenize, count_freq, top_n
stroka = input("Введите строку: ")
tablet = "1"
norm = normalize(stroka)
worlds = tokenize(norm)
unique_worls = count_freq(worlds)
top_5 = top_n(unique_worls)
if tablet:
   max_len = max([len(i[0]) for i in top_5])
   if max_len > 5:
        print("Слово"+" "*(max_len - 4)+"|"+" Частота")
        print("-"*(10 + max_len))
        for i in top_5:
            print(f"{i[0]:<{max_len}} | {i[1]}")
        print("-"*(10 + max_len))
   else:
       print("Слово | Частота")
       print("-"*15)
       for i in top_5:
            print(f"{i[0]:<{max_len}} | {i[1]}")
       print("-"*(10 + max_len))
   
else:
    print(f"Всего слов: {len(worlds)}")
    print(f"Уникальных слов: {len(unique_worls)}")
    print("Топ-5:")
    for i in top_5:
        print(f"{i[0]}:{i[1]}")