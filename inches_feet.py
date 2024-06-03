import FreeSimpleGUI as fsg
import inches_feet_meter as ifm

label1 = fsg.Text("Enter feet: ")
input1 = fsg.InputText(key="feet")

label2 = fsg.Text("Enter inches: ")
input2 = fsg.InputText(key="inches")

convert_button = fsg.Button("Convert")
result = fsg.Text(key="result")

window = fsg.Window("Convertor", layout=[[label1, input1],
                                         [label2, input2],
                                         [convert_button, result]])

while True:
    event, values = window.read()
    print(event, values)
    feet = int(values['feet'])
    inches = int(values['inches'])
    res = ifm.convert(feet, inches)
    window["result"].Update(res)
    if fsg.WIN_CLOSED:
        break

window.close()