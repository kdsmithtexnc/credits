import tkinter as tk

#Define Function to Calculate Credits
def calculate_credits():
    name = name_entry.get()
    degree = degree_entry.get()
    credits_taken = int(credits_taken_entry.get())
    total_credits = int(total_credits_entry.get())

    credits_needed = total_credits - credits_taken

    result_label.config(text=f"Name: {name}\nDegree: {degree}\nCredits left to graduate: {credits_needed}")
    
## Define Window GUI 
# Create the main window
window = tk.Tk()
window.title("Graduation Calculator")

# Create and place widgets
tk.Label(window, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

tk.Label(window, text="Degree:").grid(row=1, column=0)
degree_entry = tk.Entry(window)
degree_entry.grid(row=1, column=1)

tk.Label(window, text="Credits Taken:").grid(row=2, column=0)
credits_taken_entry = tk.Entry(window)
credits_taken_entry.grid(row=2, column=1)

tk.Label(window, text="Total Credits:").grid(row=3, column=0)
total_credits_entry = tk.Entry(window)
total_credits_entry.grid(row=3, column=1)

result_label = tk.Label(window, text="Result will be displayed here.")
result_label.grid(row=4, column=0, columnspan=2)

calculate_button = tk.Button(window, text="Calculate", command=calculate_credits)
calculate_button.grid(row=5, column=0, columnspan=2)

# Start the main event loop
window.mainloop()

