from pyfiglet import Figlet
from bot_commands import COMMANDS
from book_commands import find_same_input


def main():
    '''
    A console bot assistant that recognizes commands entered from the

    keyboard and responds according to the entered
    command.
    :return: Answers according to commands
    '''

    preview_text = Figlet(font='slant')
    print(preview_text.renderText('ProPy10'))
    print(f'Hello! Welcome to your Personal assistant. How can I help you?')

    while True:
        command = input("Please enter the command: ").lower().strip()
        try:
            for key in COMMANDS:
                if command.startswith(key):
                    command = key
                    break
            result = COMMANDS[command]()

            print(result)
        except KeyError:
            find_same_input(command, COMMANDS)


main()
