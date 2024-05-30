import FreeSimpleGUI as fsg

label1 = fsg.Text("Enter feet: ")
input1 = fsg.InputText()
choose_button1 = fsg.Button("Choose")

label2 = fsg.Text("Enter inches: ")
input2 = fsg.InputText()
choose_button2 = fsg.Button("Choose")

convert_button = fsg.Button("Convert")

window = fsg.Window("Convertor", layout=[[label1, input1, choose_button1],
                                         [label2, input2, choose_button2],
                                         [convert_button]])

window.read()
window.close()