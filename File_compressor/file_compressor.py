import FreeSimpleGUI as fsg
import Zip_creator

label1 = fsg.Text("Select files to compress: ")
input1 = fsg.Input(key="file_input")
choose1 = fsg.FilesBrowse("Choose", key="File_choose")

label2 = fsg.Text("Select the destination folder: ")
input2 = fsg.Input(key="folder_input")
choose2 = fsg.FolderBrowse("Choose", key="Folder_choose")

compress = fsg.Button("Compress")
msg = fsg.Text(key = "msg", text_color="purple")

layout = [[label1, input1, choose1],
          [label2, input2, choose2],
          [compress, msg]]
window = fsg.Window("File Compressor", layout=layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values['File_choose'].split(";")
    dest_dir = values['Folder_choose']
    Zip_creator.make_archive(filepaths, dest_dir)
    window["msg"].Update("Compressed Successfull.")

    if fsg.WIN_CLOSED:
        break
window.close()
