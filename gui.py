import tkinter as tk
import random
import string

# Function to generate the password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            result_label.config(text="Password length must be at least 1.", fg="red")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password: {password}", fg="green")
    except ValueError:
        result_label.config(text="Please enter a valid number.", fg="red")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Customize window size and background color
window.geometry("350x200")
window.configure(bg="lightgray")

# Create and place the widgets with customization
frame = tk.Frame(window, bg="lightgray")
frame.pack(expand=True)

tk.Label(frame, text="Enter the desired password length:", font=("Arial", 12), bg="lightgray").pack(pady=10)
length_entry = tk.Entry(frame, font=("Arial", 12), width=10)
length_entry.pack(pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password, font=("Arial", 12), bg="gray", fg="white")
generate_button.pack(pady=10)

result_label = tk.Label(frame, text="", font=("Arial", 12), bg="lightgray", wraplength=300)
result_label.pack(pady=10)

# Run the application
window.mainloop()
