import FreeSimpleGUI as fsg
import zip_extract

fsg.theme("DarkTeal10")

label1 = fsg.Text("Select the archive:")
input1 = fsg.Input()
choose_file = fsg.FileBrowse("Choose", key="archive")

label2 = fsg.Text("Select the destination:")
input2 = fsg.Input()
choose_folder = fsg.FolderBrowse("Choose", key="folder")

extract_button = fsg.Button("Extract")
msg = fsg.Text(key="output")

layout = [[label1, input1, choose_file],
          [label2, input2, choose_folder],
          [extract_button, msg]]
window = fsg.Window("Files Extract", layout=layout)
while True:
    event, values = window.read()
    print(event)
    print(values)
    file_to_extract = values["archive"]
    dest = values["folder"]
    zip_extract.extract_files(file_to_extract, dest)
    window["output"].update(value="File Extracted")

window.close()
