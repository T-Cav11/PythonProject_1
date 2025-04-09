import Functions
import FreeSimpleGUI as sg

label =sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task: ")
add_task_button = sg.Button("Add")

window = sg.Window("Tasks to be completed", [[label], [input_box, add_task_button]])
window.read()
window.close()


