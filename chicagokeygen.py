import tkinter as tk
import random
import hashlib

# Define a function that will be called when the button is clicked
def on_generate():
    # Retrieve the values from the textboxes
    var1 = build_entry.get()
    var2 = site_id_entry.get()
    var3 = password_entry.get()
    
    # Call the ChicagoCredentials function with the retrieved values
    credentials = ChicagoCredentials(build=var1, site=var2, password=var3)
    credentials.generate()
    result_entry.delete(0, tk.END)
    result_entry.insert(0, credentials)

class ChicagoCredentials:
    def __init__(self, site="", password="", build=""):
        self.site = site
        self.password = password
        self.build = build

    def get_text(self, build):
        build_texts = {
            "73f": "Microsoft Chicago PDK Release, November 1993",
            "73g": "Microsoft Chicago PDK2 Release, December 1993",
            "81": "Chicago Preliminary PDK Release, January 1994",
            "99": "Chicago Preliminary Beta 1 Release, May 1994",
            "122": "Chicago Beta 1 Release, May 1994",
            "216": "Windows 95 Beta 2 Release, October 1994",
            "ie4july": "Microsoft Internet Explorer 4.0 alpha 2 July 1996 release",
            "ie4sept": "Microsoft Internet Explorer 4.0 Beta - Sept. 1996 release"
        }
        if build in build_texts:
            return build_texts[build]
        else:
            raise ValueError("invalid build")

    def __str__(self):
        return f"{self.site}/{self.password}"

    def generate(self):
        site = self.site
        if not self.site:
            site = f"{random.randint(0, 999999):06d}"

        passw = self.password
        if not self.password:
            passw = f"{random.randint(0, 65535):04x}"

        hasher = hashlib.new('md4')
        try:
            text = self.get_text(self.build)
        except ValueError as e:
            return str(e)

        hasher.update(f"{site}{passw}{text}".encode('utf-8'))
        sum_hash = hasher.digest()

        last = f"{sum_hash[1:2].hex()}{sum_hash[0:1].hex()}"

        middle = 0
        for char in site + passw + last:
            middle += ord(char)

        self.site = site
        self.password = f"{passw}{middle % 9}{last}"
        return None

# Create the main window
root = tk.Tk()
root.title("Microsoft Chicago Keygen")
root.resizable(False, False)

# Create and place labels and textboxes
tk.Label(root, text="Build:").grid(row=0, column=0, padx=5, pady=5)
build_entry = tk.Entry(root, width=25)
build_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Beta Site ID:").grid(row=1, column=0, padx=5, pady=5)
site_id_entry = tk.Entry(root, width=25)
site_id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, width=25)
password_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Result:").grid(row=4, column=0, padx=5, pady=5)
result_entry = tk.Entry(root, width=25)
result_entry.grid(row=4, column=1, padx=5, pady=5)

# Create and place the button
generate_button = tk.Button(root, text="Generate", command=on_generate)
generate_button.grid(row=3, column=1, padx=5, pady=5)

# Run the application
root.mainloop()
