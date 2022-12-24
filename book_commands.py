# All ContactBook functions
import os
from difflib import get_close_matches
from book_class import ContactBook, Record, Address, Email, Birthday, CONTACTS

if os.path.exists('dump.pickle'):
    CONTACTS = ContactBook().address_book_load()
else:
    CONTACTS = ContactBook()


def name_input():
    name = input(f'Please enter contact name: ')
    return name


def address_input():
    address = input(f'Please enter contact address: ')
    return address


def phones_input():
    phones = input(f'Please enter contact phones: ')
    return phones.split()


def email_input():
    email = input(f'Please enter contact email: ')
    return email


def birthday_input():
    birthday = input(f'Please enter contact birthday: ')
    return birthday


def hello_func():
    """
    Hello Bot message

    :return: answer = string
    """

    return "How can I help you?"


# @input_error
def add_contact_func():
    '''
    Command for adding records to the dictionary
    :param command: user input
    :return: string
    '''

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


# @input_error
def add_phone_func():
    '''
    Command for adding phones to the contact
    :param command: contact book
    :return: string
    '''

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


def add_address_func():
    '''
    Command for adding address to the contact
    :param command: contact book
    :return: string
    '''

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


def add_email_func():
    '''
    Command for adding address to the contact
    :param command: contact book
    :return: string
    '''

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


def add_birthday_func():
    '''
    Command for adding address to the contact
    :param command: contact book
    :return: string
    '''

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


# @input_error
def exit_func():
    """
    "good bye", "close", "exit" on any of these commands,
    the bot terminates its work after it displays "Good bye!" in the console.
    :return: string
    """

    ContactBook().address_book_save(CONTACTS)


# @input_error
def save_contacts_to_file():
    """
    Function saves contacts to file
    :return: string
    """
    pass


# @input_error
def load_contacts_from_file():
    """
    Function loads contacts from the file
    :return: string
    """
    pass


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
