import Functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in To-Do:")
input_box = fsg.InputText(tooltip="Enter a todo: ", key="todo")
button = fsg.Button("Add")

window = fsg.Window("To-Do App",
                    layout=[[label],[input_box, button]],
                    font = ('Cambria Math', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todo = Functions.get_todos()
            new_event = values['todo']
            Functions.write_todos(new_event)

        case fsg.WIN_CLOSED:
            break

window.close()