from pathlib import Path

def total_salary(path: str):
    try:
        file_path = Path(path)        
        with file_path.open('r') as file:
            total = 0
            count = 0
            raw_lines = file.readlines()
            for count, line in enumerate(raw_lines, start=1):
                line = line.strip()
                parts = line.split(",", 1)
                if len(parts) != 2:
                    raise ValueError(f"Некоректний формат рядка: {line}")
                _, salary_str = parts
                salary = int(salary_str)
                total += salary
            average_salary = total / count
            return total, average_salary
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл не знайдено за шляхом: {path}") from e
    
        
total, average = total_salary('./salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")