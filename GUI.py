import Functions
import FreeSimpleGUI as sg

label =sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task: ", key = "task")
add_task_button = sg.Button("Add")

window = sg.Window("Tasks to be completed",
                   [[label], [input_box, add_task_button]],
                   font= ("Helvetica", 11))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            tasks = Functions.get_tasks()
            new_task = values["task"] + "\n"
            tasks.append(new_task)
            Functions.write_tasks(tasks)
        case sg.WIN_CLOSED:
            break


window.close()


