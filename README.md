# ЛР6 - CLI-утилиты с argparse (cat/grep-lite + конвертеры)

## Задание A - Текстовые утилиты (cli_text.py)
Модуль создаёт консольную утилиту с двумя подкомандами. `cat --input <путь> [-n]` выводит содержимое файла построчно, а с флагом `-n` добавляет перед каждой строкой её номер. `stats --input <путь> [--top N]` считает частоты слов в файле с помощью функций из ЛР3 (`normalize`, `tokenize`, `count_freq`, `top_n` из `src/lib/text.py`) и печатает общее число слов, число уникальных слов и топ-N самых частых слов (по умолчанию 5). Файл читается функцией `read_text` из ЛР4. Расположен в `src/lab06/cli_text.py`.

```python
import argparse
import sys
from src.lab04.io_txt_csv import read_text
from src.lib.text import normalize, tokenize, count_freq, top_n

def read_input(path: str) -> str:
    """
    Читает текстовый файл (в кодировке UTF-8) и возвращает его содержимое.

    Если файл не найден или не читается как UTF-8 - печатает понятное
    сообщение об ошибке (в stderr) и завершает программу с кодом 1.
    """
    try:
        return read_text(path)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {path}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось прочитать файл {path} в кодировке UTF-8", file=sys.stderr)
        sys.exit(1)

def run_cat(args: argparse.Namespace) -> None:
    """
    Подкоманда cat: выводит содержимое файла построчно.
    Если указан флаг -n - перед каждой строкой печатается её номер.
    """
    text = read_input(args.input)

    lines = text.splitlines()

    for number, line in enumerate(lines, start=1):
        if args.n:
            print(f"{number}: {line}")
        else:
            print(line)

def run_stats(args: argparse.Namespace) -> None:
    """
    Подкоманда stats: считает частоты слов в файле (функции из ЛР3)
    и печатает общее число слов, число уникальных слов и топ слов.
    """
    text = read_input(args.input)

    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{args.top}:")
    for word, count in top_n(freq, n=args.top):
        print(f"{word}: {count}")
    
def main() -> None:
    parser = argparse.ArgumentParser(description="CLI-утилиты для работы с текстовыми файлами")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="вывести содержимое файла", description="Выводит содержимое файла построчно.")
    cat_parser.add_argument("--input", required=True, help="путь к текстовому файлу")
    cat_parser.add_argument("-n", action="store_true", help="нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="частоты слов в тексте", description="Считает частоты слов в тексте и выводит самые частые.")
    stats_parser.add_argument("--input", required=True, help="путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="сколько слов показать (по умолчанию 5)")

    args = parser.parse_args()

    if args.command == "cat":
        run_cat(args)
    elif args.command == "stats":
        if args.top <= 0:
            parser.error("--top должен быть положительным числом")
        run_stats(args)

if __name__ == "__main__":
    main()
```

### Проверка:

people.csv
```
name,age,city
Alice,22,SPB
Bob,25,Moscow
Carlos,30,Kazan
Dana,21,SPB
Andrey,27,Novosibirsk
```

![Задание](images/lab06/img_01.png)

stats.txt
```
Привет, мир! Привет, Python!
Python - простой язык, а мир программирования большой.
Мы изучаем Python, чтобы писать простые программы.
По-настоящему интересно, когда программа работает.
Ёлка и ёжик живут в лесу, а ежик любит ёлку.
```
![Задание](images/lab06/img_02.png)

---

## Задание B - Конвертеры (cli_convert.py)
Модуль создаёт консольную утилиту с тремя подкомандами: `json2csv`, `csv2json` и `csv2xlsx`. У каждой два обязательных параметра: `--in` (входной файл) и `--out` (выходной файл). Подкоманды вызывают функции из ЛР5 (`json_to_csv`, `csv_to_json`, `csv_to_xlsx`). Расположен в `src/lab06/cli_convert.py`.

```python
import argparse
import json
import sys
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main() -> None:
    parser = argparse.ArgumentParser(description="Конвертеры данных JSON / CSV / XLSX")
    sub = parser.add_subparsers(dest="command", required=True)

    p1 = sub.add_parser("json2csv", help="преобразовать JSON в CSV", description="Преобразует JSON в CSV.")
    p1.add_argument("--in", dest="input", required=True, help="входной .json файл")
    p1.add_argument("--out", dest="output", required=True, help="выходной .csv файл")

    p2 = sub.add_parser("csv2json", help="преобразовать CSV в JSON", description="Преобразует CSV в JSON.")
    p2.add_argument("--in", dest="input", required=True, help="входной .csv файл")
    p2.add_argument("--out", dest="output", required=True, help="выходной .json файл")

    p3 = sub.add_parser("csv2xlsx", help="преобразовать CSV в XLSX", description="Преобразует CSV в файл Excel.")
    p3.add_argument("--in", dest="input", required=True, help="входной .csv файл")
    p3.add_argument("--out", dest="output", required=True, help="выходной .xlsx файл")

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {args.input}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: некорректный JSON", file=sys.stderr)
        sys.exit(1)
    except ValueError as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

```powershell
python -m src.lab06.cli_convert json2csv --in data/lab05/samples/people.json --out data/lab05/out/people.csv
python -m src.lab06.cli_convert csv2json --in data/lab05/samples/people.csv --out data/lab05/out/people.json
python -m src.lab06.cli_convert csv2xlsx --in data/lab05/samples/people.csv --out data/lab05/out/people.xlsx
```

![Задание](images/lab06/img_03.png)

![Задание](images/lab06/img_04.png)

![Задание](images/lab06/img_05.png)

---

## Способ запуска

Запуск выполняется из **корня репозитория** (там, где лежит папка `src/`), с помощью флага `-m`:

```powershell
python -m src.lab06.cli_text <подкоманда> [параметры]
python -m src.lab06.cli_convert <подкоманда> [параметры]
```
---

### Справка --help

Справка работает и для самой утилиты, и для каждой подкоманды, например:

```
python -m src.lab06.cli_text --help
usage: python.exe -m src.lab06.cli_text.py [-h] {cat,stats} ...

CLI-утилиты для работы с текстовыми файлами

positional arguments:
  {cat,stats}
    cat        вывести содержимое файла
    stats      частоты слов в тексте

options:
  -h, --help   show this help message and exit
```