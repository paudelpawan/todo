import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type in a to-do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter a todo", key="todo")
add_button = FreeSimpleGUI.Button("Add")
list_box = FreeSimpleGUI.Listbox(values = functions.get_todos(), key="todos", enable_events = True, size=[45,10])
edit = FreeSimpleGUI.Button("Edit")
window = FreeSimpleGUI.Window("My To-Do App",
                              layout=[[label], [input_box, add_button], [list_box, edit]],
                              font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"]+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos= functions.get_todos()
            index= todos.index(todo_to_edit)
            todos[index]= new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case FreeSimpleGUI.WIN_CLOSED:
            break

window.close()
