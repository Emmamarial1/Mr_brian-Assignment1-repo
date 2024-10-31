class studentsRegistery:
    def __init__(self, name, registeration_number):
        self.name = name
        self.registeration_number = registeration_number
        
        
    def dispaly_students(self):
        print(f"Student name: {self.name} Student Number: {self.registeration_number}")
        
        


student1 = studentsRegistery("EMMA MARIAL", "B22555")
student2 = studentsRegistery("MARY AMAN", "B37605")

student1.dispaly_students()
student2.dispaly_students()