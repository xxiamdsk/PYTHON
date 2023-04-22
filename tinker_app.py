import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
label = tk.Label(text="Python rocks!")
label.pack()


# Button
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="red",
)
button.pack()

# Entry
entry = tk.Entry()
entry.insert(0, "Type something here")
entry.pack()


window.mainloop()
