class Employee:
    def __init__(self, name, idnumber, department, position):
        self.name = name
        self.idnumber = idnumber
        self.department = department
        self.position = position

    def display_employee(self):

        print('{}    {}       {}     {}' .format(self.name, self.idnumber, self.department, self.position))


def main():
    emp1 = Employee('Susan Meyers', 47899, 'Accounting', '    Vice President')
    emp2 = Employee('Mark  Jones ', 39119, 'IT  Specialist', 'Programmer')
    emp3 = Employee('Joy  Rogers ', 81774, 'Manufacturing ', 'Engineer')
    print('Name\t\tID Number   Department\t       Job Title')
    emp1.display_employee()
    emp2.display_employee()
    emp3.display_employee()


if __name__ == '__main__':

    main()
