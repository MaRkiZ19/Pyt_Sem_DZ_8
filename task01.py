phone_book={}
path: str = 'sem8/phone_book.txt'


def remove():
    result=search()
    show_contacts(result)
    index=int(input('Введите id контакта под удаление '))
    del_cnt = phone_book.pop(index)
    print(f'\n Контакт {del_cnt.get("name")} успешно удален')
    print('='*200 +'\n')


def open_file():
    phone_book.clear()
    file=open(path, 'r', encoding='UTF8' )  # path - путь к файлу, r - открываем для чтения(reding),  encoding - кодировка UTF8
    data = file.readlines()
    file.close() 
    for contact in data:
        nc = contact.strip().split(':')     # strip очищает начало и конец от ненужных символов
        phone_book[int(nc[0])] = ({'name': nc[1], 'phone': nc[2], 'coment': nc[3]})
    print('\nТелефонная книга успешно загружена!')



def save_file():
    data=[]
    for i, contact in phone_book.items():
        new = ':'.join([str(i),contact.get('name'), contact.get('phone'),contact.get('coment')])
        data.append(new)
    data='\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:   # w - перезапсь
        file .write(data)
    print(f'\n Телефонная книга успешно сохранена')
    print('='*200 +'\n')


def search():
    result={}
    word = input('Введите слово для поиска ')
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
            result[i]=contact
    return result



def show_contacts(book: dict[int,dict]):
    print('\n'+ '='*200)
    for i, cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"): <20}{cnt.get("phone"): <20}{cnt.get("coment"):<20}')
    print('='*200 +'\n')



def add_contact():
    uid=max(list(phone_book.keys())) +1
    name=input('Введите имя контакта: ')
    phone=input('Введите номер телефона контакта: ')
    coment=input('Введите коментарий контакта: ')
    phone_book[uid] = {'name': name, 'phone': phone, 'coment': coment }
    print(f'\n Контакт {name} успешно добавлен')
    print('='*200 +'\n')



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


open_file()

while True:
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            print(show_contacts(phone_book))
        case 4:
            add_contact()
        case 5:
            result = search()
            show_contacts(result)
        case 6:
            pass
        case 7:
            remove()
        case 8:
            print('До свидания!')
            break
    

