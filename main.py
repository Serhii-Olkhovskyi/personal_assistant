from book_class import Record, ContactBook

def add_birthday():
    """
    Функция добавляет день рождения контакта.

    Параметры
    ---------
    :param:
    :return:
    """


def add_contact():
    """
    Функция добавляет в адресную книгу введенное имя контакта с большой буквы и его номер телефона.

    Параметры
    ---------
    :param:
    :return:
    """


def add_phone(name, new_phone):
    """
    Функция добавляет к существующему контакту еще один номер телефона.

    Параметры
    ---------
    :param:
    :return:
    """
    if name not in contacts_dict:
        raise ValueError('This contact is not in the address book.')
    
    record = Record(name)
    record.add_phone(new_phone)
    contacts_dict.add_record(record)
    return f'You added new contact: {name} with this {phones}.'


def add_email(name, email):
    if name not in contacts_dict:
        raise ValueError('This contact is not in the address book.')

    record = Record(name)
    record.add_email(email)
    contacts_dict.add_record(record)
    return f'You added new contact: {name} with this {email}.'

def change_phone():
    """
    Функция замены номера телефона существующего контакта.

    Параметры
    ---------
    :param:
    :return:
    """


def dell_phone():
    """
    Функция удаляет номер телефона у контакта.

    Параметры
    ---------
    :param:
    :return:
    """


def exit_program():
    """
    Функция завершает программу.

    Параметры
    ---------
    :param:
    :return:
    """


def func_show_all():
    """
    Функция выводит всю адресную книгу.

    Параметры
    ---------
    :param:
    :return:
    """


def func_show_birthday():
    """
    Функция выводит количество дней до следующего дня рождения контакта.

    Параметры
    ---------
    :param:
    :return:
    """


def hello():
    """
    Функция приветствия.

    Параметры
    ---------
    :param:
    :return:
    """


def main():
    """
    Основная функция для запуска программы.

    :return:
    """


def show_phone():
    """
    Функция поиска номера по имени.

    Параметры
    ---------
    :param:
    :return:
    """


if __name__ == '__main__':
    contacts_dict = ContactBook()
    main()
