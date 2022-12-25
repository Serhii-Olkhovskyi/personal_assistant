from out_table import show_out_table


def all_commands():
    """
    Функция показывает все возможные команды.

    :return: 'Enter new command.'
    """

    help_list = [
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
        ('Help on commands', 'help', '', '', '')
    ]

    table_header = ['DESCRIPTION', 'COMMAND', 'PARAMETER 1', 'PARAMETER 2', 'PARAMETER 3']
    show_out_table(help_list, table_header)

    return f'.'