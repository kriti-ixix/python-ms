class Student: #Parent/Base class
    def __init__(self, n="N/A", r=0):
        self.name = n
        self.rollno = r

    def __str__(self):
        return str(self.rollno) + ". " + self.name

class Exams(Student): #Child/Derived class
    def __init__(self, s, m, n="N/A", r=0):
        Student.__init__(self, n="N/A", r=0)
        self.subject = s
        self.marks = m

s1 = Student()
print(s1)

s2 = Student("XYZ", 10)
print(s2)

# s1 = Student("ABC", 5)
# #s1.rollno = 2
# print(s1)
# #print(s1.name)
# #print(s1.rollno)

# s2 = Student("XYZ", 10)
# print(s2)
#s2.rollno = 5
#print(s2.rollno)

#Create a list of five student class objects after getting information
#from the user

e1 = Exams("ABC", 4, "Python", 85)

