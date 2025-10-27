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