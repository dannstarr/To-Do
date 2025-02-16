FILEPATH = "files/todos.txt"

def get_todos():
    try:
        with open(FILEPATH, "r") as file:
            todos_local = file.readlines()
        return todos_local if todos_local else []
    except FileNotFoundError:
        return []  # Return an empty list if file doesn't exist


def write_todos(todos_arg, filepath = FILEPATH):
    with open(filepath, "w") as file:
        todos_local = file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())