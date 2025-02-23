import FreeSimpleGUI as sg
import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


label1 = sg.Text("Select Files To Compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select Destination Folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Zip Files")
message = sg.Text(key="message", text_color="green")

window = sg.Window("DannStarr File Zipper", layout=[[label1, input1, choose_button1],
                                                         [label2, input2, choose_button2],
                                                         [compress_button, message]])
while True:
    event, values = window.read()
    print(f"event: {event}")
    print(f"values: {values}")

    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["message"].update(value="File compression completed!")

window.close()

