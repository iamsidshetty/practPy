__author__ = 'sid'

# An example of class inheritance

class SchoolMember:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        print "Intializing School Member %s" % self.name

    def display(self):
        print "Id: %s Name: %s Age: %s" % (self.id, self.name, self.age)


class Teacher(SchoolMember):
    def __init__(self, id, name, age, course, salary):
        SchoolMember.__init__(self, id, name, age)
        self.salary = salary
        self.course = course
        print "Intializing Teacher %s" % self.name

    def display(self):
        SchoolMember.display(self)
        print "Course In-charge: %s Salary: %s" % (self.course, self.salary)


class Student(SchoolMember):
    def __init__(self, id, name, age, gpa, year):
        SchoolMember.__init__(self, id, name, age)
        self.gpa = gpa
        self.year = year
        print "Intializing Student %s" % self.name

    def display(self):
        SchoolMember.display(self)
        print "GPA: %s Year: %s" % (self.gpa, self.year)


if __name__ == "__main__":
    # Name, Age, Course, Salary
    Js = Teacher('100001', 'John Smith', 43, 'Data Mining', '$100,000')
    Mc = Teacher('100002', 'Marie Curie', 33, 'Machine Learning', '$88,000')
    Sid = Student('200001', 'Sudarshan', 23, '3.0', 'Freshman')

    print "\n"
    Members = [Js, Mc, Sid]
    for each in Members:
        each.display()


