import tkinter as tk
from tkinter import filedialog

class Notepad:

    def __init__(self, master):
        self.master = master
        master.title("Bloco de notas (by Guilherme)")
        self.text = tk.Text(master)
        self.text.pack(fill=tk.BOTH, expand=True)

        # Menu
        self.menu = tk.Menu(master)
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.file_menu.add_command(label="Novo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Salvar", command=self.save_file)
        self.file_menu.add_command(label="Sair", command=self.exit_program)
        self.menu.add_cascade(label="Arquivo", menu=self.file_menu)

        master.config(menu=self.menu)

    def new_file(self):
        self.text.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                file_content = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file_content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".text")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text.get(1.0, tk.END))

    def exit_program(self):
        self.master.quit()

root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
