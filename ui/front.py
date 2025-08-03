import tkinter as tk

def show_menu(event, menu):
    menu.tk_popup(event.x_root, event.y_root)

root = tk.Tk()
root.title("To-Do List with Actions")
root.geometry("350x250")

todos = ["Buy groceries", "Call mom", "Read a book", "Do homework"]

for i, todo in enumerate(todos):
    row = tk.Frame(root)
    row.pack(fill="x", pady=3)

    label = tk.Label(row, text=todo, anchor="w", width=22, font=("Helvetica", 13))
    label.pack(side="left", padx=(10,0))

    # Create a menu for actions
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Edit")
    menu.add_command(label="Mark as Done")
    menu.add_command(label="Delete")

    # Three dots button
    btn = tk.Button(row, text="⋮", font=("Helvetica", 15), width=2, relief="flat")
    btn.pack(side="right", padx=(0,15))
    # Bind right-click or button click to menu popup
    btn.bind("<Button-1>", lambda event, m=menu: show_menu(event, m))

root.mainloop()
