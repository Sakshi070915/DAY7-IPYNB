#1. Create a menu based Python application for maintaining student information

import tkinter as tk
from tkinter import messagebox

def main():
    students = {}  # Dictionary to store student information

    def add_student():
        rollno = entry_rollno.get()
        name = entry_name.get()
        marks = entry_marks.get()
        
        if rollno and name and marks:
            if rollno not in students:
                students[rollno] = {"name": name, "marks": marks}
                messagebox.showinfo("Success", "Student added successfully!")
                clear_entries()
            else:
                messagebox.showwarning("Error", "Roll number already exists!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def display_students():
        if students:
            display_text = ""
            for rollno, info in students.items():
                display_text += f"Roll No: {rollno}, Name: {info['name']}, Marks: {info['marks']}\n"
            messagebox.showinfo("Student Records", display_text)
        else:
            messagebox.showinfo("Student Records", "No records found.")

    def search_student():
        rollno = entry_rollno.get().strip()  # Remove any extra spaces
        
        if not rollno:
            messagebox.showwarning("Input Required", "Please enter a roll number to search!")
            return
        
        if rollno in students:
            student = students[rollno]
            messagebox.showinfo("Search Result", 
                f"Roll No: {rollno}\nName: {student['name']}\nMarks: {student['marks']}")
        else:
            messagebox.showerror("Error", "Student not found!")

    def remove_student():
        if not students:
            messagebox.showinfo("Error", "No students to remove!")
            return
        
        # Create a new window to show list of students
        remove_window = tk.Toplevel(root)
        remove_window.title("Remove Student")
        remove_window.geometry("300x400")
        
        # Label
        tk.Label(remove_window, text="Select a student to remove:").pack(pady=10)
        
        # Create buttons for each student
        for rollno, info in students.items():
            tk.Button(
                remove_window,
                text=f"Roll No: {rollno} - {info['name']}",
                command=lambda r=rollno: confirm_remove(r, remove_window)
            ).pack(fill='x', padx=20, pady=2)

    def confirm_remove(rollno, window):
        if messagebox.askyesno("Confirm", f"Are you sure you want to remove student with Roll No: {rollno}?"):
            del students[rollno]
            messagebox.showinfo("Success", "Student removed successfully!")
            window.destroy()
            clear_entries()

    def total_students():
        count = len(students)
        messagebox.showinfo("Total Students", f"Total number of student records: {count}")

    def clear_entries():
        entry_rollno.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_marks.delete(0, tk.END)

    # Create main window
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("400x300")

    # Create input fields
    tk.Label(root, text="Roll No:").grid(row=0, column=0, padx=10, pady=5)
    entry_rollno = tk.Entry(root)
    entry_rollno.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5)
    entry_name = tk.Entry(root)
    entry_name.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Marks:").grid(row=2, column=0, padx=10, pady=5)
    entry_marks = tk.Entry(root)
    entry_marks.grid(row=2, column=1, padx=10, pady=5)

    # Create buttons
    tk.Button(root, text="Add Student", command=add_student).grid(
        row=3, column=0, padx=10, pady=5)
    
    tk.Button(root, text="Display Students", command=display_students).grid(
        row=3, column=1, padx=10, pady=5)
    
    tk.Button(root, text="Search Student", command=search_student).grid(
        row=4, column=0, padx=10, pady=5)
    
    tk.Button(root, text="Remove Student", command=remove_student).grid(
        row=4, column=1, padx=10, pady=5)
    
    tk.Button(root, text="Total Students", command=total_students).grid(
        row=5, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
