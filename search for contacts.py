# decorator to handle user input errors

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError as value_error:
            return value_error
        except KeyError as key_error:
            return key_error
        except IndexError:
            return 'Please type: name and phone number'
        except TypeError:
            return "No command found. Please type one of this: hello, add [Name] [phone1] [phone2]...[birthday], " \
                   "change [Name] [old_phone] [new_phone], phone [Name], delete [Name] [phone], birthday [Name], " \
                   "pagination [page], search [content], show all, exit, good bye, close. "
        except Exception as error:
            return error

    return wrapper

@input_error
def find_contacts(user_input):
    """
    Command that displays a list of users who have a match in their name or phone number with the entered string
    :return: contacts
    """
    result = ""
    user_input = user_input.strip().capitalize()
    contacts = ADDRESS_BOOK.find_contacts(user_input) # ADDRESS_BOOK екземляр класу
    if contacts:
        for contact in contacts:
            name = contact.name.value
            all_phones = list(map(lambda x: str(x), contact.get_phones()))
            result += f"I have found {name} with phones:{', '.join(all_phones)}\n"
        return result
    return f"No matches found: {user_input[0]}"