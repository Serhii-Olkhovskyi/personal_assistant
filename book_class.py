from collections import UserDict
import re


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

    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not re.fullmatch(r"\+\d{12}", new_value):
            raise ValueError("Invalid phone number, enter the phone number in the format: (+380123456789)")
        self.__value = new_value


class Email(Field):
    """
    `Email` class, an optional field with a contact email address.
    """

    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not re.findall(r"[a-zA-Z]{1,}[a-zA-Z0-9._]{1,}[@][a-zA-Z]{1,}[.][a-zA-Z]{2,}", new_value):
            raise ValueError("Invalid email, enter in the correct format")
        self.__value = new_value


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
        self.email = email


class ContactBook(UserDict):
    """
    `ContactBook` class, which is inherited from `UserDict`,
    and is responsible for the logic of searching for records in this class.
    """

    def add_record(self, record):
        self.data[record.name.value] = record
