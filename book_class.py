import pickle
import sys
from collections import UserDict

class Field:
    """
    `Field` class, which is the parent for all fields,

    and is responsible for the logic common to all fields.
    """

    def __init__(self, value):
        self.__value = value
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    """
    `Name` class, a mandatory field with a contact name.

    """



class Address(Field):
    """
    `Address` class, an optional field with a contact address info.
    """


class Phone(Field):
    """
    `Phone` class, an optional field with a contact phone numbers.
    """

    pass


class Email(Field):
    """
    `Email` class, an optional field with a contact email address.
    """

    pass


class Birthday(Field):
    """
    `Birthday` class, an optional field with a contact birthday info.
    """



class Record:
    """
    `Record` class, which is responsible for the logic of
    adding/deleting/editing optional fields and storing the required fields.
    """

    def __init__(self, name, address=None, phones=None, email=None, birthday=None):
        self.name = Name(name)
        self.address = address if address else None
        self.phones = phones if phones else []
        self.email = email if email else None
        self.birthday = birthday if birthday else None

    def add_phone(self, phone):
        '''
        Add phone

        :param phone:
        :return:
        '''

        self.phones.append(Phone(phone))

    def get_phones(self):
        all_phones = [phone.value for phone in self.phones]
        return all_phones

    def add_email(self, email):
        self.email = Email(email)

    def add_address(self, address):
        self.address = Address(address)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def get_user_details(self):
        """
        Метод преобразует phones и дату в строку

        Параметры
        ---------
        :param:
        :return: str phone
        """

        show_phone = ''
        show_birthday = ''
        show_address = ''
        show_email = ''

        for phone in self.phones:
            show_phone += f"{phone.value}  "

        if self.birthday is None:
            show_birthday = ''
        else:
            show_birthday += f'{self.birthday.value}'

        if self.address is None:
            show_address = ''
        else:
            show_address += f'{self.address.value}'

        if self.email is None:
            show_email = ''
        else:
            show_email += f'{self.email.value}'

        return f'{self.name.value:<10} | {show_phone:<10} | {show_birthday:^15} | {show_address:<20} | {show_email}'


class ContactBook(UserDict):
    """
    `ContactBook` class, which is inherited from `UserDict`,
    and is responsible for the logic of searching for records in this class.
    """

    def add_record(self, record):
        self.data[record.name.value] = record

    def address_book_load(self):
        """
        Функция загружает адресную книгу при старте.

        Параметры
        ---------
        :param:
        :return:
        """

        with open('dump.pickle', 'rb') as dump_file:
            archive_book = pickle.load(dump_file)
            return archive_book

    def address_book_save(self, archive_book):
        """
        Функция сохраняет адресную книгу и завершает программу.

        Параметры
        ---------
        :param:
        :return:
        """

        with open('dump.pickle', 'wb') as dump_file:
            pickle.dump(archive_book, dump_file)

        sys.exit()


CONTACTS = ContactBook()
