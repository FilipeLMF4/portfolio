from tkinter import *
# https://tcl.tk/man/tcl8.6/TkCmd/contents.htm

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=100)  # Add some padding around window edges. Same works for widgets

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))  # Create
# my_label.pack()  # Display component at specified side
# my_label.place(x=0, y=0)  # Display component at specific place
my_label.grid(column=0, row=0)   # Layout along a grid (start at top left with col 0 and row 0)

# Change properties of a component
my_label["text"] = "New Text"
my_label.config(text="New Text", padx=20, pady=50)


# Button
def button_clicked():
    print("I got clicked!")
    my_label["text"] = inp.get()


button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry (basically an input)
inp = Entry(width=10)
# Add some text to begin with
inp.insert(END, string="Some text to begin with.")
inp.grid(column=3, row=2)

# Cannot use pack and grid on same file!

# Always at the end
window.mainloop()
