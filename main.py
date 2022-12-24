from difflib import get_close_matches
from book_class import ContactBook
from bot_commands import COMMANDS
import book_commands

CONTACTS = ContactBook()

def find_same_input(inp_user):
    same_input = get_close_matches(inp_user, COMMANDS.keys(), n=3, cutoff=0.7)
    return same_input

def main():
    '''
    A console bot assistant that recognizes commands entered from the keyboard and responds according to the entered
    command.
    :return: Answers according to commands
    '''

    # book_commands.hello_func()

    # Bot execution
    while True:
        command = input("Please enter the command: ").lower().strip()
        for key in COMMANDS:
            if command.startswith(key):
                command = key
                break
        result = COMMANDS[command](CONTACTS)

        print(result)


main()