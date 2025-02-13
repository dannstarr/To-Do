def get_todos(filepath):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath="files/todos.txt"):
    with open(filepath, "w") as file:
        todos_local = file.writelines(todos_arg)