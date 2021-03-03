class Employee:
    def __init__(self,fname,lname):
        self.fanem = fname
        self.lname = lname
        #self.email = f"{fanme}.{lname}@codewithharry.com

    def explain(self):
        return f"This employee is{self.fanem} {self.lname}"

    @property
    def email(self):
        if self.fanem == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fanem}.{self.lname}@codewithmezbah.com"

    @email.setter
    def email(self,string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fanme = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fanem = None
        self.lname = None

skillf = Employee("Skill", "F")
o = "this is a string"





import inspect
print(inspect.getmembers(skillf))



