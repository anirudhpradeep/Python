import tkinter as tk
from tkinter import messagebox

def find_repeated_items():
    try:
        #tuple input from the user
        user_input = tuple(map(str.strip, input_entry.get().split(',')))
        
        # Finding repeated items
        seen = set()
        repeated = set(x for x in user_input if x in seen or seen.add(x))

        # Displaying the result
        if repeated:
            result_label.config(text=f"Repeated items: {', '.join(repeated)}")
        else:
            result_label.config(text="No repeated items found.")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Creating the main window
root = tk.Tk()
root.title("Find Repeated Items in a Tuple")
root.geometry("600x400")
root.configure(bg="#e6f7ff")

# Title label
title_label = tk.Label(root, text="Tuple Repetition Checker", font=("Comic Sans MS", 20, "bold"), bg="#e6f7ff", fg="#004d99")
title_label.pack(pady=20)

# Input label and entry field
input_frame = tk.Frame(root, bg="#e6f7ff")
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Enter tuple elements:", font=("Comic Sans MS", 14), bg="#e6f7ff", fg="#004d99")
input_label.grid(row=0, column=0, padx=5)

input_entry = tk.Entry(input_frame, width=40, font=("Comic Sans MS", 14), highlightbackground="#004d99", highlightthickness=2, relief="flat")
input_entry.grid(row=0, column=1, padx=5)

# Button to find repeated items
find_button = tk.Button(root, text="Find Repeated Items", font=("Comic Sans MS", 14, "bold"), bg="#004d99", fg="white", activebackground="#0059b3", activeforeground="white", relief="raised", command=find_repeated_items)
find_button.pack(pady=20)

# Label to display the result
result_label = tk.Label(root, text="", font=("Comic Sans MS", 16), bg="#e6f7ff", fg="#cc0000")
result_label.pack(pady=20)

# Footer label
footer_label = tk.Label(root, text="Crafted with Tkinter", font=("Comic Sans MS", 12, "italic"), bg="#e6f7ff", fg="#0066cc")
footer_label.pack(side="bottom", pady=10)

# Run the main loop
root.mainloop()
