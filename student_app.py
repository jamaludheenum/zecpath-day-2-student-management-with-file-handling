class Student:
    def __init__(self,name,roll_num,grade):
        self.name=name
        self.roll_num=roll_num
        self.__grade=grade# Private attribute (Encapsulation)

    def get_average(self):
            if not self.__grade:
                return 0
            return sum(self.__grade)/ len(self.__grade)
        
    def display_info(self):
            avg=self.get_average()
            print(f"Student: {self.name} | Roll No: {self.roll_num}")
            print(f"Grades: {self.__grade} | Average: {avg:.3f}")
            print("-" * 30)

s1 = Student("Aju", "CS101", [85, 90, 80])
s2 = Student("anil", "CS102", [70, 75, 74])

s1.display_info()
s2.display_info()