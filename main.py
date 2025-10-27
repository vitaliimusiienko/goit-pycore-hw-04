from task_4_scripts_for_console_bot import parse_input, add_contact, change_contact, show_phone, show_all
    
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
    



