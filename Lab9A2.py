# Lab9A1 Getting Employee Information
# This program will provide employee name with job title, salary and years of experience

class EmployeeData(object):
    def __init__(self, nm, jt, s, yrs):
        self.name = nm
        self.jobTitle = jt
        self.salary = s
        self.years = yrs
        self.pecentRaise = 0

    def getName(self):
        return self.name

    def getTitle(self):
        return self.jobTitle

    def getSalary(self):
        return self.salary

    def getYears(self):
        return self.years
    def Raise(self, salary, percentRaise):
       self.salary = salary *(1 + percentRaise)
        
    def __str__(self):
        return  "\nemployee name: " + self.name + "\nJob Title: " + self.jobTitle + "\nsalary: " + "%0.2f" % self.salary + "\nYears of experience: " + str(self.years)

def main():
    Helen = EmployeeData("Helen Calder", "Analyst", 45000, 5)
    Fred = EmployeeData("Fred Aramis", "Accountant", 67000, 3)
    print(Helen)
    print(Fred)

    Helen.Raise(4500, 0.2)
    Fred.Raise(6700, 0.15)
    print(Helen)
    print(Fred)
    
if __name__ == "__main__":
    main()
