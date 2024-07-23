import tkinter as tk
from tkinter import messagebox
size = 0
mines = 0

def get_table_info():
    def on_submit():
        global size,mines
        try:
            size = int(size_entry.get())
            mines = int(mine_entry.get())
            if mines > (size**2)/2 :
                messagebox.showerror("Error", f"Invalid input. Please enter a valid number of mines. should be less than {(size**2)//2}")
            elif not 10<=size<=30:
                messagebox.showerror("Error", f"The game table size is invalid. the lenght of each side should be between 10 and 30 boxes")

            else:
            # Process the number here
                root.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    # Create the main application window
    root = tk.Tk()
    root.title("Table info input")

    # Create a label and an entry widget for number input
    label = tk.Label(root, text="Enter the number of squares in one side:")
    label.pack()
    size_entry = tk.Entry(root)
    size_entry.pack()
    label = tk.Label(root, text="Enter the number of mines:")
    label.pack()
    mine_entry = tk.Entry(root)
    mine_entry.pack()

    # Create a submit button to process the input
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack()
    # Start the main event loop

    root.mainloop()
    return size , mines

