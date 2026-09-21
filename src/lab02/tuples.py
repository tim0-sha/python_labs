def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec) != 3:
        raise ValueError("Введите ФИО, группу, GPA")
    fio = rec[0].split()
    group = rec[1]
    gpa = rec[2]
    answer = ""
    if len(fio) == 2:
        answer = f"{fio[0][0].upper()}{fio[0][1:].lower()} {fio[1][0].upper()}."
    elif len(fio) == 3:
        answer = f"{fio[0][0].upper()}{fio[0][1:].lower()} {fio[1][0].upper()}.{fio[2][0].upper()}."
    else:
        raise ValueError("Введите корректное ФИО")
    if len(rec[1]) == 0:
        raise ValueError("Введите корректную группу")
    if (type(gpa) == float):
        answer = str(f"{answer}, гр. {group}, GPA {round(gpa,2):.2f}")
    else:
        raise TypeError("Введите корректное GPA")
    return answer

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))