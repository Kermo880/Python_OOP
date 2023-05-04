class Pastry:
    def __init__(self, name: str, complexity_level: int):
        self.name = name
        self.complexity_level = complexity_level
    
    def __repr__(self):
        return self.name

class Baker:
    def __init__(self, name: str, experience_level: int, money: int):
        self.name = name
        self.experience_level = experience_level
        self.money = money
    
    def __repr__(self):
        return f"Baker: {self.name}({self.experience_level})"
        
class Bakery:
    def __init__(self, name: str, min_experience_level: int, budget: int):
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.bakers = []
        self.recipes = {}
        self.pastries = []
    
    def add_baker(self, baker: Baker) -> Baker:
        if isinstance(baker, Baker) and baker.experience_level >= self.min_experience_level:
            self.bakers.append(baker)
            return baker
        else:
            return None
    
    def add_recipe(self, name: str):
        if self.budget - len(name) >= 0 and name not in self.recipes and self.bakers != None:
            complexity_level = abs(len(name) * len(self.bakers) - min(baker.experience_level for baker in self.bakers))
            self.recipes[name] = complexity_level
            self.budget -= len(name)
    
    def make_order(self, name: str) -> Pastry:
        if name in self.recipes:
            eligible_bakers = [baker for baker in self.bakers if baker.experience_level >= self.recipes[name]]
            if eligible_bakers:
                baker = min(eligible_bakers, key=lambda x: abs(x.experience_level - self.recipes[name]) or 1)
                pastry = Pastry(name, self.recipes[name])
                tulu = len(name) * 4
                self.budget += tulu // 2
                self.pastries.append(pastry)
                baker.experience_level += len(name)
                baker.money += tulu // 2
                self.min_experience_level += 1
                return pastry
            else:
                return None
    
    def remove_baker(self, baker: Baker):
        if baker in self.bakers:
            self.bakers.remove(baker)
    
    def get_recipes(self) -> dict:
        return self.recipes
    
    def get_bakers(self) -> list:
        return sorted(self.bakers, key=lambda x: x.experience_level, reverse=True)
    
    def get_pastries(self) -> list:
        return sorted(self.pastries, key=lambda x: x.complexity_level, reverse=True)
    
    def __repr__(self):
        return f"Bakery {self.name}: {len(self.bakers)} baker(s)"
    
baker1 = Baker("Alice", 10, 100)
baker2 = Baker("Bob", 2, 50)
baker3 = Baker("Max", 25, 10)

bakery = Bakery("Delicious Bakery", 2, 200)

bakery.add_baker(baker1)
bakery.add_baker(baker2)
bakery.add_baker(baker3)

bakery.add_recipe("cupcake")
bakery.add_recipe("pie")

pastry = bakery.make_order("cupcake")

bakery.remove_baker(baker2)

bakers = bakery.get_bakers()
pastries = bakery.get_pastries()
recipes = bakery.get_recipes()

print(bakery)
print(bakers)
print(recipes)
print(pastries)