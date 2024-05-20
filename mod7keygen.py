import tkinter as tk
from tkinter import ttk
import random

def generate_ddd():
    """Generate a 3-digit number from 001 to 366."""
    return f"{random.randint(1, 366):03}"

def generate_yy():
    """Generate a 2-digit number from a specified set of years."""
    years = ['95', '96', '97', '98', '99', '00', '01', '02', '03']
    return random.choice(years)

def generate_xxxxxxx():
    """Generate a 7-digit number that starts with 0, the sum of its digits is divisible by 7, and it does not end in 0, 8, or 9."""
    while True:
        xxxxxx = f"{random.randint(100000, 999999)}"
        xxxxxxx = '0' + xxxxxx
        
        # Calculate the sum of digits
        digit_sum = sum(int(digit) for digit in xxxxxxx)

        # Check if conditions are met
        if digit_sum % 7 == 0 and xxxxxxx[-1] not in {'0', '8', '9'}:
            return xxxxxxx
        
def generate_zzzzz():
    """Generate a random 5-digit number."""
    return f"{random.randint(10000, 99999):05}"

def generate_number_sequence_oem():
    ddd = generate_ddd()
    yy = generate_yy()
    xxxxxxx = generate_xxxxxxx()
    zzzzz = generate_zzzzz()
    return f"{ddd}{yy}-OEM-{xxxxxxx}-{zzzzz}"

def generate_xxx():
    """Generate a 3-digit number in the range 100-999 that doesn't include 333, 444, 555, 666, 777, 888, 999."""
    invalid_nums = {333, 444, 555, 666, 777, 888, 999}
    
    while True:
        xxx = random.randint(100, 999)
        if xxx not in invalid_nums:
            return xxx

def generate_yyyyyyy():
    """Generate a 7-digit number that the sum of its digits is divisible by 7, and it does not end in 0, 8, or 9."""
    while True:
        yyyyyyy = f"{random.randint(1000000, 9999999)}"
        
        # Calculate the sum of digits
        digit_sum2 = sum(int(digit) for digit in yyyyyyy)

        # Check if conditions are met
        if digit_sum2 % 7 == 0 and yyyyyyy[-1] not in {'0', '8', '9'}:
            return yyyyyyy

def generate_number_sequence_normal():
    xxx = generate_xxx()
    yyyyyyy = generate_yyyyyyy()
    return f"{xxx}-{yyyyyyy}"

def generate_xxxx():
    while True:
        xxxx = random.randint(1, 9991)
        xxxx_str = f'{xxxx:04}'  # Ensure it's four digits, padded with leading zeros if necessary
        third_digit = int(xxxx_str[2])
        last_digit = int(xxxx_str[3])
        
        # Check if the last digit is third digit + 1 or 2 (consider overflow)
        valid_last_digit = (last_digit == (third_digit + 1) % 10 or last_digit == (third_digit + 2) % 10)
        
        if valid_last_digit:
            return xxxx_str

def generate_number_sequence_11_digits():
    xxxx = generate_xxxx()
    yyyyyyy = generate_yyyyyyy()
    return f"{xxxx}-{yyyyyyy}"
    
# Create the main window
root = tk.Tk()
root.title("Microsoft mod7 Keygen")
root.resizable(False, False)

# Create the "Your Key" label and text box
key_label = ttk.Label(root, text="Your Key:")
key_label.grid(row=1, column=0, padx=10, pady=10)
key_entry = ttk.Entry(root, width=30)
key_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# Create the "Normal" button
normal_button = ttk.Button(root, text="Normal", command=lambda: [key_entry.delete(0, tk.END), key_entry.insert(0, generate_number_sequence_normal())])
normal_button.grid(row=2, column=0, padx=10, pady=10)

# Create the "OEM" button
oem_button = ttk.Button(root, text="OEM", command=lambda: [key_entry.delete(0, tk.END), key_entry.insert(0, generate_number_sequence_oem())])
oem_button.grid(row=2, column=1, padx=10, pady=10)

# Create the "11-digit" button
digit_button = ttk.Button(root, text="11-digit", command=lambda: [key_entry.delete(0, tk.END), key_entry.insert(0, generate_number_sequence_11_digits())])
digit_button.grid(row=2, column=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()