# All ContactBook functions
import os
from difflib import get_close_matches
from book_class import ContactBook, Record, Address, Email, Birthday, CONTACTS
from datetime import datetime, timedelta, date
from input_error_handler import input_error
import re
from out_table import show_out_table


def name_input(add_contact=None):
    """
    Input name
    :return: name
    """
    while True:
        name = input(f'Please enter contact name: ').capitalize()
        if name:
            if name in CONTACTS.data.keys() and add_contact:
                print(f"Contact '{name}' has already exist in contact book.")
            elif name not in CONTACTS.data.keys() and not add_contact:
                print(f"No records with '{name}' contact found.")
            elif not name.isdigit():
                return name
            print(f"Name is a mandatory field and must not be a digit.")
        print("Name is a mandatory field. Please enter name. You didn't type anything.")


def address_input():
    """
    Input address
    :return: address
    """
    address = input(f'Please enter contact address: ')
    return address


def phones_input():
    """
    Input phones
    :return: phones list
    """
    while True:
        phones = input(f'Please enter contact phones: ')
        if not phones:
            return []
        check = True
        for number in phones.split():
            if not re.fullmatch(r"\+\d{12}", number):
                print(f"Invalid phone number:{number}, enter the phone number in the format: (+380123456789)")
                check = False
        if check:
            return phones.split()


def email_input():
    """
    Input email
    :return: email
    """
    while True:
        email = input(f'Please enter contact email: ')
        if not email:
            return email
        else:
            if not re.findall(r"[a-zA-Z]{1,}[a-zA-Z0-9._]{1,}[@][a-zA-Z]{1,}[.][a-zA-Z]{2,}", email):
                print("Invalid email, enter in the correct format: example@gmail.com")
            return email


def birthday_input():
    """
    Input birthday
    :return: birthday
    """
    while True:
        birthday = input(f'Please enter contact birthday: ')
        if not birthday:
            return birthday
        else:
            if re.search(r"\b\d{2}[.]\d{2}[.]\d{4}", birthday):
                value_split = birthday.split(".")
                birthday = date(year=int(value_split[2]), month=int(value_split[1]), day=int(value_split[0]))
                return birthday.strftime("%d.%m.%Y")
            print("Birthday must be in DD.MM.YYYY format")


def hello_func():
    """
    Hello Bot message
    :return: answer = string
    """

    return "How can I help you?"


@input_error
def add_contact_func():
    """
    Command for adding records to the contact book
    :return: string
    """

    name = name_input("yes")
    phones = phones_input()
    email = email_input()
    address = address_input()
    birthday = birthday_input()

    CONTACTS.add_record(Record(name))
    for phone in phones:
        if phone not in CONTACTS[name].get_phones():
            CONTACTS[name].add_phone(phone)
    CONTACTS[name].add_address(address)
    CONTACTS[name].add_email(email)
    CONTACTS[name].add_birthday(birthday)

    return f"Contact '{name}' was added with: phones:[{', '.join(phones)}], address: [{address}], email: [{email}], " \
           f"birthday: [{birthday}]."


@input_error
def add_phone_func():
    """
    Command for adding phones to the contact
    :return: string
    """

    name = name_input()
    phones = phones_input()

    for phone in phones:
        if phone not in CONTACTS[name].get_phones():
            CONTACTS[name].add_phone(phone)
    return f"Phones:[{', '.join(phones)}] were added to contact '{name}'."


@input_error
def add_address_func():
    """
    Command for adding address to the contact
    :return: string
    """

    name = name_input()
    address = address_input()

    if not CONTACTS[name].address.value:
        CONTACTS[name].add_address(address)
        return f"Address:{address} was added to contact '{name}'."
    raise ValueError(f"Contact '{name}' already has address record. Please enter another command to "
                     f"change address.")


@input_error
def add_email_func():
    """
    Command for adding email to the contact
    :return: string
    """

    name = name_input()
    email = email_input()

    if not CONTACTS[name].email.value:
        CONTACTS[name].add_email(email)
        return f"Email:{email} was added to contact '{name}'."
    raise ValueError(f"Contact '{name}' already has email record. Please enter another command to "
                     f"change email.")


@input_error
def add_birthday_func():
    """
    Command for adding birthday to the contact
    :return: string
    """

    name = name_input()
    birthday = birthday_input()

    if not CONTACTS[name].birthday.value:
        CONTACTS[name].add_birthday(birthday)
        return f"Birthday:{birthday} was added to contact '{name}'."
    raise ValueError(f"Contact '{name}' already has address record. Please enter another command to "
                     f"change birthday.")


@input_error
def exit_func():
    """
    "good bye", "close", "exit" on any of these commands,
    the bot terminates its work after it displays "Good bye!" in the console.
    :return: string
    """

    ContactBook().address_book_save(CONTACTS)


@input_error
def find_same_input(inp_user, command):
    """
    Analyzes the entered text and tries to guess what the user wants from it.

    :param inp_user: str
    :return:
    """

    list_commands = []
    for elem in command.keys():
        list_commands.append(elem)

    same_input = get_close_matches(inp_user, list_commands, n=3, cutoff=0.4)
    print()
    print('Such a command does not exist.')
    print('The following commands might work:')
    for elem in same_input:
        print(elem)
    print()


@input_error
def show_all_info():
    """
    Функция выводит всю адресную книгу.

    Параметры
     ---------
    :param:
    :return:
    """
    info_data = []
    for users in CONTACTS.values():
        info_data.append(users.get_user_details())

    table_header = ('Name', 'Phones', 'Birthday', 'Address', 'Email',)
    show_out_table(info_data, table_header)

    return f'ok.'


@input_error
def list_birthday():
    days = int(input(f'Please enter number of days: '))
    today = datetime.today()
    end_day = today + timedelta(days)
    count = 0
    lst = "Birthday of this period:"
    for name in CONTACTS:
        bday = CONTACTS[name].birthday.value
        bday = datetime.strptime(bday, "%Y.%m.%d").date()
        if datetime(today.year, bday.month, bday.day) <= today:
            nday = datetime(today.year + 1, bday.month, bday.day)
        else:
            nday = datetime(today.year, bday.month, bday.day)
        if nday <= end_day:
            lst += f'\n{name}: {CONTACTS[name].birthday.value}'
            count += 1
    return lst if count > 0 else f'No one birthday at this period'


@input_error
def change_phone_func():
    """
    Command for change phone of the contact
    :return: string
    """

    name = name_input()

    while True:
        print(f'Contact number to change.')
        phone_old = phones_input()
        if phone_old in CONTACTS[name].get_phones():
            print(f'New contact number to record.')
            phone_new = phones_input()
            CONTACTS[name].change_phone(phone_old, phone_new)
            return f"{name}`s phone is changed from {phone_old} to {phone_new}."
        print(f"Contact '{name}' doesn't have such phone number: {phone_old}.")


@input_error
def change_email_func():
    """
    Command for change email of the contact
    :return: string
    """

    name = name_input()

    while True:
        email = email_input()
        if email:
            CONTACTS[name].change_email(email)
            return f"{name}`s email is changed to {email}."
        print("Please enter email.You didn't type anything.")


@input_error
def change_address_func():
    """
    Command to change address of the contact
    :return: string
    """

    name = name_input()

    while True:
        address = address_input()
        if address:
            CONTACTS[name].change_adress(address)
            return f"{name}`s address is changed to {address}."
        print("Please enter address.You didn't type anything.")


@input_error
def change_birthday_func():
    """
    Command to change birthday of the contact
    :return: string
    """
    name = name_input()
    while True:
        birthday = birthday_input()
        if birthday:
            CONTACTS[name].change_birthday(birthday)
            return f"{name}`s birthday is changed to {birthday}."
        print("Please enter birthday.You didn't type anything.")


@input_error
def delete_phone_func():
    """
    Command to delete phone of the contact
    :return: string
    """
    name = name_input()

    while True:
        print("Phone to delete.")
        phone = phones_input()
        if phone in CONTACTS[name].get_phones():
            CONTACTS[name].delete_phone(phone)
            return f"{name}`s phone number '{phone}' was deleted."
        print(f"{name} have no such phone number '{phone}'.")


@input_error
def delete_email_func():
    """
    Command to delete email of the contact
    :return: string
    """
    name = name_input()
    CONTACTS[name].delete_email()
    return f"{name}`s email is deleted."


@input_error
def delete_address_func():
    """
    Command to delete address of the contact
    :return: string
    """
    name = name_input()
    CONTACTS[name].delete_address()
    return f"{name}`s address is deleted."


@input_error
def delete_birthday_func():
    """
    Command to delete birthday of the contact
    :return: string
    """
    name = name_input()
    CONTACTS[name].delete_birthday()
    return f"{name}`s `birthday` is deleted."


@input_error
def delete_contact_func():
    """
    Command to delete contact
    :return: string
    """
    name = name_input()
    CONTACTS.delete_contact(name)
    return f"Contact '{name}' is deleted."


@input_error
def show_birthday():
    name = name_input()
    if name in CONTACTS.data.keys():
        if CONTACTS[name].birthday:
            today = datetime.today()
            bday = datetime.strptime(CONTACTS[name].birthday.value, "%d.%m.%Y").date()
            if datetime(today.year, bday.month, bday.day) <= today:
                nday = datetime(today.year + 1, bday.month, bday.day)
            else:
                nday = datetime(today.year, bday.month, bday.day)
            timediff = (nday - today).days + 1
            # timediff = (nday - today).days + 1 if (today - nday).days < 0 else (datetime(nday.year + 1, nday.month, nday.day) - today).days + 1
            return f'{timediff} days till {name} birthday left!'
        return f"Contact '{name}' hasn`t birthday record. Please enter another command to add birthday"
    return f"No records with '{name}' contact found. Type another contact name"


@input_error
def phone():
    name = name_input()
    if name in CONTACTS.data.keys():
        if CONTACTS[name].phones:
            return f"{name}: {', '.join([phone.value for phone in CONTACTS[name].phones])}"
        return f"Contact '{name}' hasn't any phone record. Please enter another command to add phone"
    return f"No records with '{name}' contact found. Type another contact name"


def find_contacts():
    name = input("enter the contact name to search: ")
    data = name.strip().title()
    matches_list = []
    for users in CONTACTS.values():
        if users.name.value == data:
            matches_list.append(users.get_user_details())
    if matches_list:
        table_header = ('Name', 'Phones', 'Birthday', 'Address', 'Email')
        show_out_table(matches_list, table_header)
        return "Contact found"
    return f"No matches were found."
