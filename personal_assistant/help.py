from out_table import show_out_table


def all_commands():
    """
    Функция показывает все возможные команды.

    :return: 'Enter new command.'
    """

    help_list = [
        ('hello', 'Greeting'),
        ('exit', 'Exit the program and save the data'),
        ('close', 'Close program and save data'),
        ('good bye', 'Close program and save data'),
        ('add contact', 'Create a new contact with the following fields'),
        ('add phone', 'Add a new phone number to an existing contact'),
        ('add address', 'Add an address to an existing contact'),
        ('add email', 'Add an email address to an existing contact'),
        ('add birthday', 'Add a birthday to an existing contact'),
        ('add note', 'Add notes'),
        ('change phone', 'Change the phone number of an existing contact'),
        ('change address', 'Change the address of an existing contact'),
        ('change email', 'Change the mailbox of an existing contact'),
        ('change birthday', 'Change the birthday of an existing contact'),
        ('edit note', 'Edit notes'),
        ('delete phone', 'Delete the phone number of an existing contact'),
        ('delete address', 'Delete an address from an existing contact'),
        ('delete email', "Delete an existing contact's mailbox"),
        ('delete birthday', 'Delete the birthday of an existing contact'),
        ('delete contact', 'Delete an existing contact'),
        ('delete note', 'Delete notes'),
        ('find note', 'Find notes'),
        ('show all contacts', 'View all contacts'),
        ('show notes', 'View notes'),
        ('phone', 'Look up a phone number based on the name of an existing contact'),
        ('birthday', 'List users whose birthday is in N days'),
        ('help', 'Command table')
        ]

    table_header = ['COMMAND', 'DESCRIPTION']
    show_out_table(help_list, table_header)

    return f'.'