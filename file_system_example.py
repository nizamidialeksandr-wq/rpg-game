"""
Простой пример: сохранение словаря на диск и чтение обратно.
Запуск: python3 save_example.py
"""
 
import json
from pathlib import Path
 
# Файл, куда пишем и откуда читаем
FILE = Path("example_save.json")
 
 
def save(data):
    """Записать словарь data в JSON-файл."""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Сохранено в {FILE}")
 
 
def load():
    """Прочитать JSON-файл и вернуть словарь."""
    if not FILE.exists():
        print("Файла ещё нет")
        return None
 
    with open(FILE, encoding="utf-8") as f:
        data = json.load(f)
    print(f"Прочитано из {FILE}")
    return data
 
 
# --- демо ---
hero = {
    "name": "Воин",
    "health": 150,
    "damage": 20,
    "level": 1,
}
 
print("1) Пишем на диск:")
save(hero)
 
print("\n2) Читаем с диска:")
loaded = load()
print(loaded)