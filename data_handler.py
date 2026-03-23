import json
import os

File="student_data.json"

def load_data():
    if not os.path.exists(File):
        return []
    with open(File, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
    
def save_data(data):
        with open(File,'w')as file:
             json.dump(data,file, indent=4)
        
def add_student(name,role):
        data = load_data()
        new_student ={"id":len(data)+1,"name":name,"role":role}
        data.append(new_student)
        save_data(data)
        print(f"Added: {name}")

def list_students():
        data = load_data()
        print("\n--- Student List ---")
        for student in data:
            print(f"ID: {student['id']} | Name: {student['name']} | Role: {student['role']}")


add_student("John Doe", "Backend Developer")
add_student("Jane Smith", "Frontend Developer")
list_students()