FILEPATH = 'todos.txt'

def print_hi(name):
    """
    :param name:
    :return: Prints a message to the name argument.
    """
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def print_todo(todos_arg):
    """
    :param todos_arg:
    :return: Take a todo list and prints out each element.
    """
    for index, todo in enumerate(todos_arg):
        todo = todo.strip('\n')
        print(f"{index + 1}.{todo}")


def write_todos(todo_arg, filepath=FILEPATH):
    """
    :param todo_arg:
    :param filepath:
    :return: Opens a text file and writes a line delimited list of to-dos.
    """
    with open(filepath, 'w') as file:
        todo_arg = [todo + "\n" for todo in todo_arg]
        file.writelines(todo_arg)


def get_todos(filepath=FILEPATH):
    """
    :param filepath:
    :return: Read a text file and return the list of to-do items.
    """
    with open(filepath, 'r') as file:
        todos_arg = file.readlines()
        todos_arg = [todo.replace("\n", "") for todo in todos_arg]
    return todos_arg


def validate_selection(todos_arg):
    """
    :param todos_arg:
    :return: Validates that the item number selected is contained
        in the to-do list index and returns the item number.
    """
    validation_check = True
    while validation_check:
        try:
            item_num_arg = int(input("Enter the item number you would like to select: "))
            selected_todo = todos_arg[item_num_arg - 1].strip('\n')
            user_validation = input(f"You have chosen: '{selected_todo}' \nIs this correct? [y/n]")
            match user_validation:
                case 'y':
                    break
                case 'n':
                    validate_selection(todos_arg)
                    break
                case _:
                    print("Hey, you entered an unknown command!")
        except (ValueError, IndexError):
            print("You entered an incorrect value!")
    return item_num_arg

if __name__ == '__main__':
    print("Hello from functions!")