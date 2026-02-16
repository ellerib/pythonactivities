from information import person

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
