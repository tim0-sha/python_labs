import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.replace("\t"," ")
    text = text.replace("\r"," ")
    text = text.replace("\n"," ")
    if yo2e:
            text = text.replace("ё", "е")
            text = text.replace("Ё","Е")
    if casefold:
        text = text.casefold()
    text = " ".join(text.split())
    return text.strip()
"""
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка", yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
"""
def tokenize(text: str) -> list[str]:
     tokens = re.findall("\w+(?:-\w+)*", text)
     return tokens
"""
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
"""
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for i in tokens:
            if i in freq:
               freq[i] += 1
            else:
                 freq[i] = 1
    return freq
"""
print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))
"""
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
     sort_freq = sorted(freq.items(), key=lambda x: (-x[1],x[0]))
     return sort_freq[:n]
"""
print(top_n(count_freq(["a","b","a","c","b","a"])n = 2))
print(top_n(count_freq(["bb","aa","bb","aa","cc"]),n = 2))
"""





# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]

# count_freq + top_n
freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}
assert top_n(freq, 2) == [("a",3), ("b",2)]

# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]