# All ContactBook functions
import os
from difflib import get_close_matches
from book_class import ContactBook, Record, Address, Email, Birthday, CONTACTS
from datetime import datetime, timedelta, date
from input_error_handler import input_error
import re

from out_table import show_out_table

if os.path.exists('dump.pickle'):
    CONTACTS = ContactBook().address_book_load()
else:
    CONTACTS = ContactBook()


def name_input():
    """
    Input name
    :return: name
    """
    while True:
        name = input(f'Please enter contact name: ')
        if name:
            if name in CONTACTS.data.keys():
                print(f"No records with '{name}' contact found. Type another contact name to add phone.")
            elif not name.isdigit():
                return name
            else:
                print(f"Name is a mandatory field and must not be a digit.")
        else:
            print("Name is a mandatory field. Please enter name. You didn't type anything.")


def address_input():
    """
    Input address
    :return: address
    """
    address = input(f'Please enter contact address: ')
    if address:
        return address
    else:
        return ''


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
            return ''
        else:
            if not re.findall(r"[a-zA-Z]{1,}[a-zA-Z0-9._]{1,}[@][a-zA-Z]{1,}[.][a-zA-Z]{2,}", email):
                print("Invalid email, enter in the correct format: example@gmail.com")
            else:
                return email


def birthday_input():
    """
    Input birthday
    :return: birthday
    """
    while True:
        birthday = input(f'Please enter contact birthday: ')
        if not birthday:
            return ''
        else:
            if re.search(r"\b\d{2}[.]\d{2}[.]\d{4}", birthday):
                value_split = birthday.split(".")
                birthday = date(year=int(value_split[2]), month=int(value_split[1]), day=int(value_split[0]))
                return birthday.strftime("%d.%m.%Y")
            else:
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

    name = name_input()
    phones = phones_input()
    email = email_input()
    address = address_input()
    birthday = birthday_input()

    CONTACTS.add_record(Record(name))
    for phone in phones:
        if phone not in CONTACTS[name].get_phones():
            CONTACTS[name].add_phone(phone)
    CONTACTS[name].address = Address(address)
    CONTACTS[name].email = Email(email)
    CONTACTS[name].birthday = Birthday(birthday)

    return f"Contact {name} was added with: phones:[{', '.join(phones)}], address: [{address}], email: [{email}], " \
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

    CONTACTS[name].add_address(address)
    return f"Address:{address} was added to contact '{name}'."


@input_error
def add_email_func():
    """
    Command for adding email to the contact
    :return: string
    """

    name = name_input()
    email = email_input()

    if not CONTACTS[name].email:
        CONTACTS[name].add_email(email)
        return f"Email:{email} was added to contact '{name}'."
    else:
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

    if not CONTACTS[name].birthday:
        CONTACTS[name].add_birthday(birthday)
        return f"Birthday:{birthday} was added to contact '{name}'."
    else:
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

    table_header = ('Name', 'Phones', 'Birthday', 'Email', 'Address')
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
        else:
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
        else:
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
        else:
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
        else:
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
        else:
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
        else:
            return f"Contact '{name}' hasn`t birthday record. Please enter another command to add birthday"
    else:
        return f"No records with '{name}' contact found. Type another contact name"


@input_error
def phone():
    name = name_input()
    if name in CONTACTS.data.keys():
        if CONTACTS[name].phones:
            return f"{name}: {', '.join([phone.value for phone in CONTACTS[name].phones])}"
        else:
            return f"Contact '{name}' hasn't any phone record. Please enter another command to add phone"
    else:
        return f"No records with '{name}' contact found. Type another contact name"


def find_contacts(name):
    data = name.strip().lower()
    matches_list = []
    for record in CONTACTS.values():

        if data in record.name.value.lower():
            matches_list.append(record.name.value)

        elif data.isdigit():
            for number in record.phones:
                if data in number.value:
                    matches_list.append(record.name.value)

    return _show_contact(matches_list)


def _show_contact(matches):
    if len(matches) == 0 or matches is None:
        return f"Збігів не знайдено."

    elif len(matches) > 0:
        return_text = ""

        for match in matches:
            return_text += f"Збіг в контакті - {match}\n"

        return return_text
