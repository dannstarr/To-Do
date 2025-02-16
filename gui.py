import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    todos = functions.get_todos()

    match event:
        case "Add":
            new_todo = values["todo"].strip()
            if not new_todo:
                continue  # Prevent adding empty todos

            todos.append(new_todo + "\n")
            functions.write_todos(todos)

            window['todo'].update("")  # Clear input box
            window['todos'].update(values=todos)  # Refresh list

        case "Edit":
            if values["todos"]:  # Check if an item is selected
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"].strip()
                if not new_todo:
                    continue  # Prevent empty edits

                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)

                window['todos'].update(values=todos)

        case "todos":
            if values["todos"]:  # Avoid IndexError
                window['todo'].update(value=values['todos'][0])

window.close()
