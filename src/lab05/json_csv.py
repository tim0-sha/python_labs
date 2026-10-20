from pathlib import Path
import json
import csv

from src.lab04.io_txt_csv import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте.
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    if not json_file.exists():
        raise FileNotFoundError("Файл не найден")
    if json_file.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат входного файла: ожидается .json")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат выходного файла: ожидается .csv")
    
    with json_file.open('r', encoding='utf-8') as p:
        try:
            data = json.load(p)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError('Файл JSON пустой или имеет неправильный формат')
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы списка JSON должны быть словарями")
    
    ensure_parent_dir(csv_file)
    fieldnames = {}
    for element in data:
        for key in element.keys():
            fieldnames[key] = None
    with csv_file.open('w', newline="", encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames.keys()))
        w.writeheader()
        w.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError("Файл не найден")
    if json_file.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат входного файла: ожидается .json")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат выходного файла: ожидается .csv")
    
    with csv_file.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("Файл CSV не содержит заголовок")
        data = list(reader)
    if not data:
        raise ValueError("Файл CSV не содержит данных")
    ensure_parent_dir(json_file)

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)



if __name__ == '__main__':
    csv_to_json(r'data\lab05\samples\people.csv',
                r'data\lab05\out\people_from_csv.json')
    json_to_csv(r'data\lab05\samples\people.json',
                r'data\lab05\out\people_from_json.csv')
    csv_to_json(r'data\lab05\samples\cities.csv',
                    r'data\lab05\out\cities_from_csv.json')
    json_to_csv(r'data\lab05\samples\cities.json',
                    r'data\lab05\out\cities_from_json.csv')