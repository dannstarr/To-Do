import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select Destination Folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

zip_button = sg.Button("zip")

window = sg.Window("File Zipper",
                   layout=[[label1, input1, choose_button1],
                          [label2, input2, choose_button2],
                           [zip_button]])

window.read()
window.close()