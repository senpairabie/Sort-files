
import tkinter as tk
from tkinter import filedialog
import os

def organize_files():
    path = filedialog.askdirectory()

    files = os.listdir(path)

    extensions = {}
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            extension = file.split(".")[-1]
            if extension in extensions:
                extensions[extension] += 1
            else:
                extensions[extension] = 1

    for extension, count in extensions.items():
        folder_name = extension_entry.get() + "_" + extension
        os.mkdir(os.path.join(path, folder_name))
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith(f".{extension}")]
        for file in files:
            os.rename(os.path.join(path, file), os.path.join(path, folder_name, file))
    
    tk.messagebox.showinfo("Organize Files", "Files organized successfully!")

root = tk.Tk()

extension_label = tk.Label(root, text="Folder Name Prefix:")
extension_label.pack()
extension_entry = tk.Entry(root)
extension_entry.pack()

button = tk.Button(root, text="Organize Files", command=organize_files)
button.pack()

root.mainloop()

