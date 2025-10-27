from pathlib import Path

def get_cats_info(path):
    try:
        file_path = Path(path)
        cats = []
        with file_path.open('r') as file:
            for line in file:
                line = line.strip()
                raw_lines = line.split(',', 2)                  
                parts = [p.strip() for p in raw_lines]
                if len(parts) != 3:
                    raise ValueError(f"Некоректний формат рядка: {line}")
                id, name, age = parts
                cats.append({"id": id, "name": name, "age": age})
            return cats
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл не знайдено за шляхом: {path}") from e
    
    
cats_info = get_cats_info("./cats_file.txt")
print(cats_info)
    
