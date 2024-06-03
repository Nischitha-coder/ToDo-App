import Functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in To-Do:")
input_box = fsg.InputText(tooltip="Enter a todo: ", key="todo")
add_button = fsg.Button("Add")

list_box = fsg.Listbox(values=Functions.get_todos(), key="todos",
                       enable_events=True, size=[45,10])
edit_button = fsg.Button("Edit")

complete_button = fsg.Button("Complete")

exit_button = fsg.Button("Exit")

layout = [[label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]
          ]
window = fsg.Window("To-Do App", layout=layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todo = Functions.get_todos()
            new_event = values['todo'] + '\n'
            todo.append(new_event)
            Functions.write_todos(todo)
            window["todos"].update(values=todo)
            window["todo"].update(value="")

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_event = values['todo'] + '\n'
            todos = Functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_event
            Functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Complete":
            todo_to_completed = values["todo"]
            todos = Functions.get_todos()
            todos.remove(todo_to_completed)
            Functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break

        case fsg.WIN_CLOSED:
            break

window.close()