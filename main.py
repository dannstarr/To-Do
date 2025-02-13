import functions
import time

now = time.ctime()
print(now)


while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit' ").strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:] +'\n'

        todos = functions.get_todos("files/todos.txt")

        todos.append(todo)

        functions.write_todos(todos, "files/todos.txt")

    elif user_action.startswith("show"):
        todos = functions.get_todos("files/todos.txt")

        for index, item in enumerate(todos):
            row = f"{index +1}- {item}"
            print(row, end="")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos("files/todos.txt")

            new_todo = input("Enter new ToDo: ") + "\n"
            todos[number] = new_todo

            functions.write_todos(todos, "files/todos.txt")
        except ValueError:
            print("Invalid selection. Type 'edit' followed by the number of your todo you'd like to edit - for example 'edit 2'")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number -= 1

            todos = functions.get_todos("files/todos.txt")

            todo_to_remove = todos[number]
            todos.pop(number)

            message = f"'{number+1}- {todo_to_remove.strip('\n')}' was successfully removed"
            print(message)

            functions.write_todos(todos, "files/todos.txt")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):

        break
    else:
        print("You entered an invalid statement. Please try again")

print("Bye!")