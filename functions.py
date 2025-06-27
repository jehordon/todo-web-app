FILEPATH = 'todos.txt'


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


if __name__ == '__main__':
    print("Hello from functions!")
