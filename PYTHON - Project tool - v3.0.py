import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class ProjectTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Tool")
        self.root.geometry("600x500")

        self.tasks = []

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.add_menus()

        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.task_entry = ttk.Entry(self.main_frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.add_task_button = ttk.Button(self.main_frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=5, pady=5)

        self.search_entry = ttk.Entry(self.main_frame, width=40)
        self.search_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.search_button = ttk.Button(self.main_frame, text="Search", command=self.search_task)
        self.search_button.grid(row=1, column=1, padx=5, pady=5)

        self.task_list = tk.Listbox(self.main_frame, width=50, height=15)
        self.task_list.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.delete_task_button = ttk.Button(self.main_frame, text="Delete Selected", command=self.delete_task)
        self.delete_task_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.complete_button = ttk.Button(self.main_frame, text="Mark Completed", command=self.mark_completed)
        self.complete_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.sort_button = ttk.Button(self.main_frame, text="Sort Tasks A-Z", command=self.sort_tasks)
        self.sort_button.grid(row=5, column=0, columnspan=2, pady=5)

    def add_menus(self):
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Save Tasks", command=self.save_tasks)
        file_menu.add_command(label="Load Tasks", command=self.load_tasks)
        file_menu.add_separator()
        file_menu.add_command(label="Settings", command=self.open_settings)
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            self.task_list.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Warning", "No task selected!")

    def mark_completed(self):
        selected = self.task_list.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            if not task.startswith("[✓]"):
                self.tasks[index] = "[✓] " + task
                self.task_list.delete(index)
                self.task_list.insert(index, self.tasks[index])
        else:
            messagebox.showwarning("Warning", "No task selected!")

    def sort_tasks(self):
        self.tasks.sort()
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

    def search_task(self):
        keyword = self.search_entry.get().strip().lower()
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            if keyword in task.lower():
                self.task_list.insert(tk.END, task)

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                for task in self.tasks:
                    f.write(task + "\n")
            messagebox.showinfo("Saved", "Tasks saved successfully!")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                self.tasks = [line.strip() for line in f.readlines()]
            self.task_list.delete(0, tk.END)
            for task in self.tasks:
                self.task_list.insert(tk.END, task)
            messagebox.showinfo("Loaded", "Tasks loaded successfully!")

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("300x200")

        ttk.Label(settings_window, text="Settings").pack(pady=10)
        ttk.Label(settings_window, text="Background Color").pack(pady=5)
        color_var = tk.StringVar(value="white")
        color_entry = ttk.Entry(settings_window, textvariable=color_var)
        color_entry.pack(pady=5)

        def apply_settings():
            bg_color = color_var.get()
            self.main_frame.config(bg=bg_color)
            settings_window.destroy()

        apply_button = ttk.Button(settings_window, text="Apply", command=apply_settings)
        apply_button.pack(pady=10)

    def show_about(self):
        messagebox.showinfo("About", "Project Tool v1.0\nCreated with Python and Tkinter.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectTool(root)
    root.mainloop()
