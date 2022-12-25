from collections import UserDict
import re
from datetime import date


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
    pass


class Address(Field):
    """
    `Address` class, an optional field with a contact address info.
    """
    pass


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
    pass


class Record:
    """
    `Record` class, which is responsible for the logic of
    adding/deleting/editing optional fields and storing the required fields.
    """

    def __init__(self, name, address=None, phones=None, email=None, birthday=None):
        self.name = Name(name)
        self.address = address
        self.phones = []
        self.email = email
        self.birthday = birthday

    def add_phone(self, phone):
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

    def change_phone(self, phone, new_phone):
        for item in self.phones:
            if item.value == phone:
                item.value = new_phone

    def change_email(self, new_email):
        self.email = Email(new_email)

    def change_address(self, new_address):
        self.address = Address(new_address)

    def change_birthday(self, new_birthday):
        self.birthday = Birthday(new_birthday)

    def delete_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)

    def delete_email(self):
        self.email = None

    def delete_address(self):
        self.address = None

    def delete_birthday(self):
        self.birthday = None

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

    def add_email(self, email):
        self.email = email


class ContactBook(UserDict):
    """
    `ContactBook` class, which is inherited from `UserDict`,
    and is responsible for the logic of searching for records in this class.
    """

    def add_record(self, record):
        self.data[record.name.value] = record
