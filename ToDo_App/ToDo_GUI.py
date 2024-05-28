import FreeSimpleGUI as fsg

label = fsg.Text("Type in To-Do:")
input_box = fsg.InputText(tooltip="Enter a todo: ")
button = fsg.Button("Add")

window = fsg.Window("To-Do App", layout=[[label],[input_box, button]])
window.read()
window.close()