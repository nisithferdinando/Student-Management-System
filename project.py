import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600+0+0")

        self.students = {}

        
        title_label = tk.Label(self.root, text="Student Management System", font=("sans-serif", 25), bg="purple", fg="white", width=800)
        title_label.grid(row=0, column=0, columnspan=5, pady=(0, 20))

       #student's details group box 
        self.groupbox_student_details = tk.LabelFrame(self.root, text="Student's Details", bg="#cfe2f3", font=("sans-serif", 14))   
        self.groupbox_student_details.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        
        self.label_name = tk.Label(self.groupbox_student_details, text="Name:", bg="#cfe2f3", font=("sans-serif", 11))
        self.entry_name = tk.Entry(self.groupbox_student_details, width=25)

        self.label_id = tk.Label(self.groupbox_student_details, text="Student ID:", bg="#cfe2f3", font=("sans-serif", 11))
        self.entry_id = tk.Entry(self.groupbox_student_details, width=25)

        self.label_gender = tk.Label(self.groupbox_student_details, text="Gender:", bg="#cfe2f3", font=("sans-serif", 11))
        self.gender_var = tk.StringVar()
        self.gender_combobox = ttk.Combobox(self.groupbox_student_details, textvariable=self.gender_var, values=["Male", "Female"], width=23)

        self.label_age = tk.Label(self.groupbox_student_details, text="Age:", bg="#cfe2f3", font=("sans-serif", 11))
        self.entry_age = tk.Entry(self.groupbox_student_details, width=25)

        self.label_degree = tk.Label(self.groupbox_student_details, text="Degree Program:", bg="#cfe2f3", font=("sans-serif", 11))
        self.entry_degree = tk.Entry(self.groupbox_student_details, width=25)
        
        #groupbox details align
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_id.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_id.grid(row=1, column=1, padx=10, pady=10)

        self.label_gender.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.gender_combobox.grid(row=2, column=1, padx=10, pady=10)

        self.label_age.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.entry_age.grid(row=3, column=1, padx=10, pady=10)

        self.label_degree.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.entry_degree.grid(row=4, column=1, padx=10, pady=10)

        
        #buttons in the group box
        self.add_button = tk.Button(self.groupbox_student_details, text="Add", command=self.add_student, width=15, bg="purple", fg="white")
        self.view_button = tk.Button(self.groupbox_student_details, text="View All", command=self.view_students, width=15, bg="purple", fg="white")
        self.search_button = tk.Button(self.groupbox_student_details, text="Search", command=self.search_student, width=15, bg="purple", fg="white")
        self.delete_button = tk.Button(self.groupbox_student_details, text="Delete", command=self.delete_student, width=15, bg="purple", fg="white")
        self.update_button = tk.Button(self.groupbox_student_details, text="Update", command=self.update_student, width=15, bg="purple", fg="white")
       
       #table details
       
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Gender", "Age", "Degree"), show="headings")
        self.tree.heading("ID", text="Student ID", anchor="center")
        self.tree.heading("Name", text="Name", anchor="center")
        self.tree.heading("Gender", text="Gender", anchor="center")
        self.tree.heading("Age", text="Age", anchor="center")
        self.tree.heading("Degree", text="Degree Program", anchor="center")
        self.tree.column("ID", width=100, anchor="center")
        self.tree.column("Name", width=150, anchor="center")
        self.tree.column("Gender", width=100, anchor="center")
        self.tree.column("Age", width=50, anchor="center")
        self.tree.column("Degree", width=150, anchor="center")

       
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("TkDefaultFont", 10, "bold"))

        
        self.tree.tag_configure("evenrow", background="#edf5fc")
        self.tree.tag_configure("oddrow", background="#cfe2f3")

        #buttons align
        self.add_button.grid(row=5, column=0, padx=10, pady=10, columnspan=1)
        self.view_button.grid(row=5, column=1, padx=10, pady=10, columnspan=1)
        self.search_button.grid(row=5, column=2, padx=10, pady=10, columnspan=1)
        self.delete_button.grid(row=5, column=3, padx=10, pady=10, columnspan=1)
        self.update_button.grid(row=5, column=4, padx=10, pady=10, columnspan=1)

        self.tree.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.groupbox_student_details.grid_rowconfigure(5, weight=0)
        self.groupbox_student_details.grid_columnconfigure(5, weight=0)

    def add_student(self):
        name = self.entry_name.get()
        student_id = self.entry_id.get()
        gender = self.gender_var.get()
        age = self.entry_age.get()
        degree = self.entry_degree.get()

        if not name or not student_id or not gender or not age or not degree:
            messagebox.showerror("Error", "All fields must be filled")
            return

        if student_id in self.students:
            messagebox.showerror("Error", "Student ID already exists")
            return

        self.students[student_id] = {"Name": name, "Gender": gender, "Age": age, "Degree": degree}
        messagebox.showinfo("Success", "Student added successfully")

        
        row_color = "evenrow" if len(self.students) % 2 == 0 else "oddrow"
        self.tree.insert("", "end", values=(student_id, name, gender, age, degree), tags=(row_color,))

        self.clear_entries()

    def view_students(self):
       
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not self.students:
            messagebox.showinfo("Information", "No students to display")
            return

        for idx, (id, info) in enumerate(self.students.items()):
           
            row_color = "evenrow" if idx % 2 == 0 else "oddrow"
            self.tree.insert("", "end", values=(id, info['Name'], info['Gender'], info['Age'], info['Degree']), tags=(row_color,))

    def search_student(self):
        student_id = self.entry_id.get()

        if student_id not in self.students:
            messagebox.showinfo("Information", f"No student found with ID {student_id}")
            return

       
        for item in self.tree.get_children():
            self.tree.delete(item)

        info = self.students[student_id]
       
        row_color = "evenrow" if len(self.students) % 2 == 0 else "oddrow"
        self.tree.insert("", "end", values=(student_id, info['Name'], info['Gender'], info['Age'], info['Degree']), tags=(row_color,))

    def delete_student(self):
        student_id = self.entry_id.get()

        if student_id not in self.students:
            messagebox.showinfo("Information", f"No student found with ID {student_id}")
            return

        confirmation = messagebox.askyesno("Confirmation", f"Do you want to delete the student with ID {student_id}?")

        if confirmation:
            del self.students[student_id]
            messagebox.showinfo("Success", "Student deleted successfully")

          
            for item in self.tree.get_children():
                self.tree.delete(item)

           
            self.view_students()

            self.clear_entries()

    def update_student(self):
        student_id = self.entry_id.get()

        if student_id not in self.students:
            messagebox.showinfo("Information", f"No student found with ID {student_id}")
            return

        name = self.entry_name.get()
        gender = self.gender_var.get()
        age = self.entry_age.get()
        degree = self.entry_degree.get()

        if name:
            self.students[student_id]['Name'] = name

        if gender:
            self.students[student_id]['Gender'] = gender

        if age:
            self.students[student_id]['Age'] = age

        if degree:
            self.students[student_id]['Degree'] = degree

        messagebox.showinfo("Success", "Student information updated successfully")

      
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.view_students()

        self.clear_entries()
 

 #clear function after the data entered or updated
    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_id.delete(0, tk.END)
        self.gender_combobox.set("")
        self.entry_age.delete(0, tk.END)
        self.entry_degree.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
