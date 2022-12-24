# All ContactBook functions
from difflib import get_close_matches
from book_class import Record, Address, Email, Birthday


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


# @input_error
def hello_func():
    """
    Hello Bot message

    :return: answer = string
    """

    return "How can I help you?"


# @input_error
def add_contact_func(contacts):
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

    if name not in contacts.data.keys():
        contacts.add_record(Record(name))
        if phones:
            for phone in phones:
                if phone not in contacts[name].get_phones():
                    contacts[name].add_phone(phone)

        if address:
            contacts[name].address = Address(address)

        if email:
            contacts[name].email = Email(email)

        if birthday:
            contacts[name].birthday = Birthday(birthday)

        return f"Contact {name} was added with: phones:[{', '.join(phones)}], address: {address}, email: {email}, birthday: [{birthday}]"


# @input_error
def exit_func():
    """
    "good bye", "close", "exit" on any of these commands,
    the bot terminates its work after it displays "Good bye!" in the console.
    :return: string
    """
    return "Good bye!"


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

    same_input = get_close_matches(inp_user, list_commands, n=3, cutoff=0.7)
    print('Such a command does not exist.')
    print('The following commands might work:')
    for elem in same_input:
        print(elem)
