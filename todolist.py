import random
import tkinter
import tkinter.messagebox

# Create a window
window = tkinter.Tk()
window.title("To Do List")
window.geometry("350x370")

tasks = []

# Functions
def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    task = txt_input.get()
    if task:
        if task not in tasks:
            tasks.append(task)
            update_listbox()
            txt_input.delete(0, "end")  # Input alanını temizle
        else:
            tkinter.messagebox.showwarning("Warning", "This task is already in the list.")
    else:
        tkinter.messagebox.showwarning("Warning", "You need to enter a task.")

def delete_all():
    confirmed = tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete all tasks?")
    if confirmed:
        global tasks
        tasks = []
        update_listbox()

def delete():
    selected_task_index = lb_tasks.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_listbox()

def sort():
    tasks.sort()
    update_listbox()

def show_number_of_task():
    number_of_task = len(tasks)
    msg = "Number of tasks: %s" % number_of_task
    lbl_display["text"] = msg

def quit():
    window.quit()

# Title
main_title = tkinter.Label(window, text="To Do List", font=("Comic Sans MS", 20))
main_title.pack()

# Printing the field I want to add to the list.
def on_enter_press(event):
    add_task()
    
txt_input = tkinter.Entry(window, width=55)
txt_input.pack(pady=5)

# We have enabled the user to start directly from the tile and easily perform the operation linked to the "Enter" key.
txt_input.bind("<Return>", on_enter_press)
txt_input.focus_set()

# Let's create frames for the buttons.
button_frame = tkinter.Frame(window)
button_frame.pack()

# Let's create a button.
buton_add = tkinter.Button(button_frame, text="Add Task", fg="black", bg="white", width=20, command=add_task, relief="flat", highlightbackground="white", highlightcolor="white")
buton_add.grid(row=0, column=0, padx=5, pady=3)

buton_delete_all = tkinter.Button(button_frame, text="Delete All", fg="black", bg="white", width=20, command=delete_all, relief="flat", highlightbackground="white", highlightcolor="white")
buton_delete_all.grid(row=1, column=0, padx=5, pady=3)

buton_delete = tkinter.Button(button_frame, text="Delete", fg="black", bg="white", width=20, command=delete, relief="flat", highlightbackground="white", highlightcolor="white")
buton_delete.grid(row=2, column=0, padx=5, pady=3)

buton_sort = tkinter.Button(button_frame, text="Sort", fg="black", bg="white", width=20, command=sort, relief="flat", highlightbackground="white", highlightcolor="white")
buton_sort.grid(row=0, column=1, padx=5, pady=3)

buton_show_number_of_task = tkinter.Button(button_frame, text="Show Number of Tasks", fg="black", bg="white", width=20, command=show_number_of_task, relief="flat", highlightbackground="white", highlightcolor="white")
buton_show_number_of_task.grid(row=1, column=1, padx=5, pady=3)

buton_quit = tkinter.Button(button_frame, text="Exit", fg="black", bg="white", width=20, command=quit, relief="flat", highlightbackground="white", highlightcolor="white")
buton_quit.grid(row=2, column=1, padx=5, pady=3)

# Let's create an area where we can see the task list.
lb_tasks = tkinter.Listbox(window, width=50, height=10)
lb_tasks.pack(padx=10, pady=10)

# Label to display random task or number of tasks
lbl_display = tkinter.Label(window, text="", font=("Helvetica", 12))
lbl_display.pack()

window.mainloop()