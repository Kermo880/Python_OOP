class Human:
    name = "Mike"
    
    def looking_for_help(self):
        print("Can you help me?")
    
    def broken(self):
        print("I have pain in my leg.")

class Doctor:
    name = "David"
    
    def heal(human):
        print("Yes, I can help you. What seems to be the problem?")

class Kirurg:
    name = "Alice"
    
    def op(docktor):
        print("Your leg seems to be broken. Let me operate on it.")

class Boss:
    name = "Mary"
    
    def boss_around(kirurg):
        print("Are you people doing your jobs here?")

print(f"Hi, my name is {Human.name}.")
mike = Human()
mike.looking_for_help()

print(f"Nice to meet you, {Human.name}. I'm Doctor {Doctor.name}.")
david = Doctor()
david.heal()

mike.broken()

print(f"Hi I'm Kirurg {Kirurg.name}.")
alice = Kirurg()
alice.op()

print(f"Hi Guys, I'm the boss here, name's {Boss.name}.")
mary = Boss()
mary.boss_around()

mike.op()