class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f"{self.name} ({self.age}) is greeting you!")

person = Person("Mike",25,"Male")

person.greet()