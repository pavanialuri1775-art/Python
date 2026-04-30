#
class Employee:
    def mainrole(self):
        print("works well")
class developer(Employee):
    def smartrole(self):
        print("works smartly")
c1=developer()
c1.mainrole()
c1.smartrole()