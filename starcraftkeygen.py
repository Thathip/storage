import tkinter as tk
from tkinter import ttk
import random

class StarCraft:
    def __init__(self):
        self.key = ""  # 15-character key (including separators), of which the last digit is a check digit

    def __str__(self):
        return f"{self.key[0:4]}-{self.key[4:9]}-{self.key[9:13]}"

    def generate(self):
        key = f"{random.randint(0, 999999999999):012d}"
        self.key = key + str(self.generate_check_digit(key))

    def generate_check_digit(self, key):
        temp = 3
        for i in range(12):
            try:
                c = int(key[i])
            except ValueError:
                return 0
            temp += (2 * temp) ^ c
        return temp % 10

# Example usage:
sc = StarCraft()

root = tk.Tk()
root.title("Starcraft Keygen")
root.resizable(False, False)

# Create the "Your Key" label and text box
key_label = ttk.Label(root, text="Your Key:")
key_label.grid(row=1, column=0, padx=10, pady=10)
key_entry = ttk.Entry(root, width=30)
key_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# Create the "OEM" button
oem_button = ttk.Button(root, text="Generate", command=lambda: [key_entry.delete(0, tk.END), sc.generate(), key_entry.insert(0, sc)])
oem_button.grid(row=2, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()
