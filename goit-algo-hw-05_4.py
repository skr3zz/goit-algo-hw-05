def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid format"
        except KeyError:
            return "Contact not found"  
    return inner
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use 'change [name] [new_phone]'"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated successfully"
@input_error
def show_contact(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Use 'show [name]'"
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]
@input_error
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "show":
            print(show_contact(args, contacts))

        elif command == "all":
            print(show_all_contacts(contacts))

        elif command == "phone":
            if len(args) != 1:
                print("Invalid command format. Use 'phone [name]'")
            else:
                name = args[0]
                if name not in contacts:
                    print("Contact not found.")
                else:
                    print(f"Phone number for {name}: {contacts[name]}")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
 #