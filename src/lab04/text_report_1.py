from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
import sys

def main():
    try:
        raw_text = read_text("data/lab04/input.txt", encoding="utf-8")
    except FileNotFoundError:
        print("Ошибка: файл не найден")
        return
    norm = normalize(raw_text)
    words = tokenize(norm)
    unique_words = count_freq(words)
    all_rows = sorted(unique_words.items(), key=lambda x: (-x[1], x[0]))
    top_5 = top_n(unique_words)
    write_csv(all_rows, "data/lab04/report.csv", header=("word", "count"))
    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(unique_words)}")
    print("Топ-5:")
    for i in top_5:
        print(f"{i[0]}: {i[1]}")

if __name__ == "__main__":
    main()
