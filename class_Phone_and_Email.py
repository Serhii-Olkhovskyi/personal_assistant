import re


class Field:
    """
    Батьківський клас для Email, Phone.
    """

    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Email(Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not re.findall(r"[a-zA-Z]{1,}[a-zA-Z0-9._]{1,}[@][a-zA-Z]{1,}[.][a-zA-Z]{2,}", new_value):
            raise ValueError("Invalid email, enter in the correct format")
        self.__value = new_value


class Phone(Field):
    """
    The phone number of the contact.
    Added to the list of phones, which is created when initializing the Record class.
    """

    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not re.fullmatch(r"\+\d{12}", new_value):
            raise ValueError("Invalid phone number, enter the phone number in the format: (+380123456789)")
        self.__value = new_value
