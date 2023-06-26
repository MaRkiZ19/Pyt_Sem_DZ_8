phone_book={}


def open_file(path: str = 'sem8/phone_book.txt'):
    phone_book.clear()
    file=open(path, 'r', encoding='UTF8' )  # path - путь к файлу, r - открываем для чтения(reding),  encoding - кодировка UTF8
    data = file.readlines()
    file.close() 
    for contact in data:
        nc = contact.strip().split(':')     # strip очищает начало и конец от ненужных символов
        phone_book[int(nc[0])] = ({'name': nc[1], 'phone': nc[2], 'coment': nc[3]})
    print('\nТелефонная книга успешно загружена!')

def show_contacts(book: dict[int,dict]):
    print('\n'+ '='*200)
    for i, cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"): <20}{cnt.get("phone"): <20}{cnt.get("coment"):<20}')
    print('='*200 +'\n')

def add_contact():
    cur_id=max(list(phone_book.keys()))
    print(cur_id)
    name=input('Введите имя контакта: ')
    phone=input('Введите номер телефона контакта: ')
    coment=input('Введите коментарий контакта: ')


def menu() -> int:
    main_menu = ''':Главное меню
    1. Открыть фаил
    2. Сохранить фаил
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)
    while True:
        select = input('Выберете пункт меню: ')
        if select.isdigit() and 0<int(select)<9:
            return int(select)
        print('Ошибка ввода, ввдите число от 1 до 8')

while True:
    open_file()
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            pass
        case 3:
            print(show_contacts(phone_book))
        case 4:
            add_contact()
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            print('До свидания!')
            break
    

