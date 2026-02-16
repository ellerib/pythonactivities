# PERSON CLASS
class person:
    #getter and setter
    #setter
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
         
        if age > 0:
            self._age = age         
        else:
            print ("Age is negative it must be positive")
    
    def set_address(self, address):
        self._address = address
    
     # getter
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_address(self):
        return self._address

    def display_info(self):
        print("Name: ", self.get_name())
        print("Age: ", self.get_age())
        print("Address: ", self.get_address())
        #return (f"Name: get_name() \n Age: {self._age} \n Address: {self._age}")   

# INFORMATION CLASS
class information():
    def __init__(self):
        self._information = []
    
    def addpersoninfo(self):
       self._information.append(person)

    def showallinfo(self):
        for p in self._information:
            print("-----")
            p.displayinfo()
            
# MAIN
database = information()

name = input("Enter name: ")
age = int(input("Enter age: "))
address = input("Enter address: ")

person = person(name, age, address)
database.addpersoninfo(person)

database.showallinfo()

