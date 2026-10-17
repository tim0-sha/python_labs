from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
import sys
from pathlib import Path

def main():
    raw_text_full = sorted(sys.argv[1:])
    raw_text_all  = ""
    per_file = []
    for i in range(len(raw_text_full)):
        try:
            raw_text = read_text(raw_text_full[i], encoding="utf-8")
        except FileNotFoundError:
            print("Ошибка: файл не найден")
            return
        raw_text_all = raw_text_all + " " + raw_text
        norm = normalize(raw_text)
        worlds = tokenize(norm)
        unique_worls = count_freq(worlds)
        sort_freq = sorted(unique_worls.items(), key=lambda x: (-x[1],x[0]))
        for w,c in sort_freq:
            per_file.append((Path(raw_text_full[i]).name,w,c))
    write_csv(per_file, "data/lab04/report_per_file.csv", header=("file","word", "count"))
    norm = normalize(raw_text_all)
    worlds = tokenize(norm)
    unique_worls = count_freq(worlds)
    top_5 = top_n(unique_worls)
    write_csv(top_5, "data/lab04/report_total.csv", header=("word", "count"))

    max_len = max([len(i[0]) for i in top_5])
    print(f"Всего слов: {len(worlds)}")
    print(f"Уникальных слов: {len(unique_worls)}")
    print("Топ-5:")
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

if __name__ == "__main__":
    main()