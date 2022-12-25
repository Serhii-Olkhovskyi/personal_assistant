from tabulate import tabulate


def all_commands():
    """
    Функция показывает все возможные команды.

    :return: 'Enter new command.'
    """

    help_list = [
        ('DESCRIPTION', 'COMMAND', 'PARAMETER 1', 'PARAMETER 2', 'PARAMETER 3'),
        ('Add contact', 'add', 'name', 'phone_number', ''),
        ('Add phone for contact', 'add_phone', 'name', 'phone_number', ''),
        ('Add birthday contact', 'add_birthday', 'name', 'YYYY.MM.DD', ''),
        ('Dell phone for contact', 'dell_phone', 'name', 'phone_number', ''),
        ('Change phone contact', 'change', 'name', 'old_phone_number', 'new_phone_number'),
        ('Show phone contact', 'phone', 'name', '', ''),
        ('Show all contacts', 'show_all', '', '', ''),
        ('Show how many days until birthday', 'show_birthday', 'name', '', ''),
        ('Show paging output', 'show_page', 'number', '', ''),
        ('Search by content in a book', 'search', 'text', '', ''),
        ('Greetings', 'hello', '', '', ''),
        ('Save contacts and close the program', 'close', '', '', ''),
        ('Save contacts and close the program', 'exit', '', '', ''),
        ('Save contacts and close the program', 'good_bye', '', '', ''),
        ('Add note', 'add note', '', '', ''),
        ('Search by notes', 'find note', '', '', ''),
        ('Show all notes', 'show notes', '', '', ''),
        ('Edit note', 'edit note', '', '', ''),
        ('Delete note', 'delete note', '', '', ''),
        ('Help on commands', 'help', '', '', '')
    ]

    print(tabulate(help_list, headers='firstrow', tablefmt='pipe', stralign='center'))
    return 'Enter new command.'
