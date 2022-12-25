# All ContactBook functions
import os
from difflib import get_close_matches
from book_class import ContactBook, Record, Address, Email, Birthday, CONTACTS
from datetime import datetime, timedelta
from input_error_handler import input_error

if os.path.exists('dump.pickle'):
    CONTACTS = ContactBook().address_book_load()
else:
    CONTACTS = ContactBook()


@input_error
def name_input():
    """
    Input name
    :return: name
    """
    name = input(f'Please enter contact name: ')
    return name


@input_error
def address_input():
    """
    Input address
    :return: address
    """
    address = input(f'Please enter contact address: ')
    return address


@input_error
def phones_input():
    """
    Input phones
    :return: phones list
    """
    phones = input(f'Please enter contact phones: ')
    return phones.split()


@input_error
def email_input():
    """
    Input email
    :return: email
    """
    email = input(f'Please enter contact email: ')
    return email


@input_error
def birthday_input():
    """
    Input birthday
    :return: birthday
    """
    birthday = input(f'Please enter contact birthday: ')
    return birthday


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
    address = address_input()
    phones = phones_input()
    email = email_input()
    birthday = birthday_input()

    if name not in CONTACTS.data.keys():
        CONTACTS.add_record(Record(name))
        if phones:
            for phone in phones:
                if phone not in CONTACTS[name].get_phones():
                    CONTACTS[name].add_phone(phone)

        if address:
            CONTACTS[name].address = Address(address)

        if email:
            CONTACTS[name].email = Email(email)

        if birthday:
            CONTACTS[name].birthday = Birthday(birthday)

        return f"Contact {name} was added with: phones:[{', '.join(phones)}], address: {address}, email: {email}, " \
               f"birthday: [{birthday}] "


@input_error
def add_phone_func():
    """
    Command for adding phones to the contact
    :return: string
    """

    name = name_input()
    phones = phones_input()

    if name in CONTACTS.data.keys():
        if phones:
            for phone in phones:
                if phone not in CONTACTS[name].get_phones():
                    CONTACTS[name].add_phone(phone)
                return f"Phones:[{', '.join(phones)}] were added to contact '{name}'."
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to add phone.")


@input_error
def add_address_func():
    """
    Command for adding address to the contact
    :return: string
    """

    name = name_input()
    address = address_input()

    if name in CONTACTS.data.keys():
        if address:
            if not CONTACTS[name].address:
                CONTACTS[name].add_address(address)
                return f"Address:{address}] was added to contact '{name}'."
            else:
                raise ValueError(f"Contact '{name}' already has address record. Please enter another command to "
                                 f"change address.")
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to add address.")


@input_error
def add_email_func():
    """
    Command for adding email to the contact
    :return: string
    """

    name = name_input()
    email = email_input()

    if name in CONTACTS.data.keys():
        if email:
            if not CONTACTS[name].email:
                CONTACTS[name].add_email(email)
                return f"Email:{email} was added to contact '{name}'."
            else:
                raise ValueError(f"Contact '{name}' already has email record. Please enter another command to "
                                 f"change email.")
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to add email.")


@input_error
def add_birthday_func():
    """
    Command for adding birthday to the contact
    :return: string
    """

    name = name_input()
    birthday = birthday_input()

    if name in CONTACTS.data.keys():
        if birthday:
            if not CONTACTS[name].birthday:
                CONTACTS[name].add_birthday(birthday)
                return f"Birthday:{birthday} was added to contact '{name}'."
            else:
                raise ValueError(f"Contact '{name}' already has address record. Please enter another command to "
                                 f"change birthday.")
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to add birthday.")


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

    for users in CONTACTS.values():
        print(users.get_user_details(), )

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
    phone_old = input(f'Please enter phone number to change: ')
    phone_new = input(f'Please enter new phone number: ')

    if name in CONTACTS.data.keys():
        if phone_old and phone_new:
            if phone_old in CONTACTS[name].get_phones():
                CONTACTS[name].change_phone(phone_old, phone_new)
                return f"{name}`s phone is changed from {phone_old} to {phone_new}."
            else:
                raise ValueError(f"Contact '{name}' doesn't have such phone number: {phone_old}.")
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to change phone.")


@input_error
def change_email_func():
    """
    Command for change email of the contact
    :return: string
    """

    name = name_input()
    email = email_input()

    if name in CONTACTS.data.keys():
        if email:
            CONTACTS[name].change_email(email)
            return f"{name}`s email is changed to {email}."
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to change email.")


@input_error
def change_address_func():
    """
    Command to change address of the contact
    :return: string
    """

    name = name_input()
    address = address_input()

    if name in CONTACTS.data.keys():
        if address:
            CONTACTS[name].change_adress(address)
            return f"{name}`s address is changed to {address}."
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to change address.")


@input_error
def change_birthday_func():
    """
    Command to change birthday of the contact
    :return: string
    """

    name = name_input()
    birthday = birthday_input()

    if name in CONTACTS.data.keys():
        if birthday:
            CONTACTS[name].change_birthday(birthday)
            return f"{name}`s birthday is changed to {birthday}."
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to change birthday.")


@input_error
def delete_phone_func():
    """
    Command to delete phone of the contact
    :return: string
    """

    name = name_input()
    phone = phones_input()

    if name in CONTACTS.data.keys():
        if phone in CONTACTS[name].get_phones():
            CONTACTS[name].delete_phone(phone)
            return f"{name}`s phone number '{phone}' was deleted."
        else:
            return f"{name} have no such phone number '{phone}'."
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to delete phone.")


@input_error
def delete_email_func():
    """
    Command to delete email of the contact
    :return: string
    """

    name = name_input()

    if name in CONTACTS.data.keys():
        CONTACTS[name].delete_email()
        return f"{name}`s email is deleted."
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to delete email.")


@input_error
def delete_address_func():
    """
    Command to delete address of the contact
    :return: string
    """

    name = name_input()

    if name in CONTACTS.data.keys():
        CONTACTS[name].delete_address()
        return f"{name}`s address is deleted."
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to delete address.")


@input_error
def delete_birthday_func():
    """
    Command to delete birthday of the contact
    :return: string
    """

    name = name_input()

    if name in CONTACTS.data.keys():
        CONTACTS[name].delete_birthday()
        return f"{name}`s `birthday` is deleted."
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to delete birthday.")


@input_error
def delete_contact_func():
    """
    Command to delete contact
    :return: string
    """

    name = name_input()

    if name in CONTACTS.data.keys():
        CONTACTS.delete_contact(name)
        return f"Contact '{name}' is deleted."
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name.")

@input_error
def show_birthday():
    name =  name_input()
    if name in CONTACTS.data.keys():
        if CONTACTS[name].birthday:
            return f"{name} birthday: {CONTACTS[name].birthday.value}"
        else:
            return f"Contact '{name}' hasn`t birthday record. Please enter another command to add birthday"
    else:
        return f"No records with '{name}' contact found. Type another contact name"


@input_error
def phone():
    name =  name_input()
    if name in CONTACTS.data.keys():
        if CONTACTS[name].phones:
            return f"{name}: {', '.join([phone.value for phone in CONTACTS[name].phones])}"
        else:
            return f"Contact '{name}' hasn`t any phone record. Please enter another command to add phone"
    else:
        return f"No records with '{name}' contact found. Type another contact name"
