from pathlib import Path
from colorama import Fore
from typing import Dict

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
    

def vizualize_directory_path(path: str, indent: int = 0):
    directory = Path(path)
    
    for path in directory.iterdir():
        prefix = " " * indent
        if path.is_dir():
            print(Fore.BLUE + f"{prefix}{path.name}/")
            vizualize_directory_path(path, indent + 1)
        else:
            print(Fore.GREEN + f"{prefix}{path.name}")
            
vizualize_directory_path("./")
        

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Недостатньо данних, вказуйте у форматі <Ім'я> <Номер телефону>"
    elif len(args) > 2:
        return "У вхідних данних забагато значень, вказуйте у форматі <Ім'я> <Номер телефону>"
    name, phone = args
    contacts[name] = phone
    return "Контакт додано"

def change_contact(args, contacts):
    if len(args) < 2:
        return "Недостатньо данних, вказуйте у форматі <Ім'я> <Новий номер телефону>"
    elif len(args) > 2:
        return "У вхідних данних забагато значень, вказуйте у форматі <Ім'я> <Новий номер телефону>"
    name, phone = args
    if name not in contacts:
        return "Данного контакту немає у списку контактів"
    contacts[name] = phone
    return "Контакт оновлено"

def show_phone(args, contacts):
    if len(args) != 1:
        return "Для комманди використовуйте тільки ім'я контакту"
    name = args[0]
    if name not in contacts:
        return "Данного контакту немає у списку контактів"
    return contacts[name]
    
def show_all(contacts):
    if not contacts:
        return "Контактів не знайдено"
    return contacts
    

def main():
    print("Вітаю у боті-ассистенті")
    contacts = {}
    while True:
        user_input = input("Введіть команду: ")
        if not user_input:
            continue
        command, *args = parse_input(user_input)
        
        match command:
            case "exit"|"close": 
                print("До побачення!")
                break
            case "hello":
                print("Чим можу допомогти?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case "help":
                print(
                    "Доступні команди: \n"
                    "  hello\n"
                    "  add <Ім'я> <Номер телефону> \n"
                    "  change <Ім'я> <Номер телефону> \n"
                    "  phone <Ім'я> \n"
                    "  all\n"
                    "  close | exit"
                                    )
            case _:
                print("Невалідна команда, скористайтесь командою help, щоб дізнатись про доступні команди")
                
if __name__ == "__main__":
    main()
    



