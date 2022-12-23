"""
Всі функціі, що стосуються книги
"""


def list_birthday(user_input):
    user_input = user_input.split()
    days = int(user_input[0])
    today = datetime.today()
    end_day = today + timedelta(days)
    lst = "Birthday of this period:"
    for name in CONTACTS:
        bday = CONTACTS[name].birthday.value
        if datetime(today.year, bday.month, bday.day) <= today:
            nday = datetime(today.year + 1, bday.month, bday.day)
        else:
            nday = datetime(today.year, bday.month, bday.day)
        if nday <= end_day:
            lst += f'\n{name}: {CONTACTS[name].birthday.value}'
    return lst