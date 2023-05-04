from typing import List


class Trainers:
    def __init__(self, stamina: int, color: str):
        self.stamina = stamina
        self.color = color
    
    def __repr__(self):
        return f"Trainers: [{self.stamina}, {self.color}]"

class Member:
    def __init__(self, name: str, age: int, trainers: Trainers):
        self.name = name
        self.age = age
        self.trainers = trainers
        self.gyms = []

    def get_all_gyms(self) -> list:
        return self.gyms
    
    def get_gyms(self) -> list:
        return [gym.name for gym in self.gyms]
    
    def has_name(self, name: str) -> bool:
        return self.name.lower() == name.lower()

    def __repr__(self):
        return f"{self.name}, {self.age}: {self.trainers}"

class Gym:
    def __init__(self, name: str, max_members_number: int):
        self.name = name
        self.max_members_number = max_members_number
        self.members = []
        self.trainers = []
        
    def add_member(self, member: Member) -> Member:
        if self.can_add_member(member):
            if len(self.members) < self.max_members_number:
                self.members.append(member)
                self.trainers.append(member.trainers)
                return member
            else:
                low_stamina_members = sorted(self.members, key=lambda m: m.trainers.stamina)
            if member.trainers.stamina > low_stamina_members[0].trainers.stamina:
                self.members.remove(low_stamina_members[0])
                self.trainers.remove(low_stamina_members[0].trainers)
                self.members.append(member)
                self.trainers.append(member.trainers)
                low_stamina_members[0].gyms.remove(self)
                return member
        else:
            return None

    def can_add_member(self, member: Member) -> bool:
        if not isinstance(member, Member):
            return False
        if member in self.members:
            return False
        if member.trainers is None:
            return False
        if member.trainers.color is None or member.trainers.stamina < 0:
            return False
        return True

    def remove_member(self, member: Member):
        if member in self.members:
            self.members.remove(member)
            member.gyms.remove(self)


    def get_max_stamina_gyms(self) -> list:
        max_stamina = 0
        for member in self.members:
            if hasattr(member, 'trainers') and member.trainers is not None:
                max_stamina += member.trainers.stamina
        return max_stamina

    def get_members_number(self) -> int:
        return len(self.members)
    
    def get_all_members(self) -> list:
        return self.members
    
    def get_average_age(self):
        if len(self.members) == 0:
            return 0
        total_age = 0
        for member in self.members:
            total_age += member.age
        return total_age / len(self.members)
    
    def get_max_average_ages(self) -> List[str]:
        if not self.members:
            return []
        max_average_age = max(self.get_average_age() for m in self.members)
        return [self.name for m in self.members if self.get_average_age() == max_average_age]

    def get_min_average_ages(self) -> List[str]:
        if not self.members:
            return []
        min_average_age = min(self.get_average_age() for m in self.members)
        return [self.name for m in self.members if self.get_average_age() == min_average_age]
    
    def __repr__(self):
        return f"Gym {self.name}: {len(self.members)} member(s)"
    
class City:
    def __init__(self, max_gym_number: int):
        self.max_gym_number = max_gym_number
        self.gyms = []

    def build_gym(self, gym: Gym) -> Gym:
        if self.can_build_gym(gym):
            self.gyms.append(gym)
            return gym
        else:
            return None
    
    def can_build_gym(self, gym: Gym) -> bool:
        if len(self.gyms) >= self.max_gym_number:
            return False
        return True if gym.name not in [g.name for g in self.gyms] else False

    def destroy_gym(self):
        if not self.gyms:
            return
        min_members = min([g.get_members_number() for g in self.gyms])
        min_gyms = [g for g in self.gyms if g.get_members_number() == min_members]
        for g in min_gyms:
            self.gyms.remove(g)

    def get_max_members_gym(self) -> list:
        if not self.gyms:
            return []
        
        max_members = max(gym.get_members_number() for gym in self.gyms)
        max_member_gyms = [gym.name for gym in self.gyms if gym.get_members_number() == max_members]
        return max_member_gyms
    
    def get_all_gyms(self) -> list:
        return self.gyms
    
    def get_gyms_by_name(self, name):
        matching_gyms = []
        for gym in self.gyms:
            for member in gym.members:
                if member.name == name:
                    matching_gyms.append(gym)
                    break
        return matching_gyms

    def get_gyms_by_trainers_color(self, color):
        matching_gyms = []
        for gym in self.gyms:
            for trainer in gym.trainers:
                if trainer.color == color:
                    matching_gyms.append(gym)
                    break
        return matching_gyms
    
city = City(2)

gym1 = Gym(name="Gym A", max_members_number=2)
gym2 = Gym(name="Gym B", max_members_number=2)

city.build_gym(gym1)
city.build_gym(gym2)

trainers1 = Trainers(stamina=10, color="red")
trainers2 = Trainers(stamina=8, color="blue")

member1 = Member(name="Bob", age=25, trainers=trainers1)
member2 = Member(name="Alice", age=30, trainers=trainers2)
member3 = Member(name="Mike", age=26, trainers=trainers1)

gym1.add_member(member1)
member1.gyms.append(gym1)
gym1.add_member(member2)
member2.gyms.append(gym1)
gym1.add_member(member3)
member3.gyms.append(gym1)

members = gym1.get_all_members()
for member in members:
    print(member.name)

print(member1.get_gyms())
print(member2.get_gyms())
print(member3.get_gyms())

print(gym1.get_max_stamina_gyms())
print(gym1.get_members_number())
print(gym1.get_average_age())

print(city.get_all_gyms())
print(city.get_gyms_by_name("Bob"))
print(city.get_gyms_by_trainers_color("red"))

gym1.remove_member(member1)
print(gym1.get_max_stamina_gyms())

city.destroy_gym()
print(len(city.gyms))

print(city.get_max_members_gym())