
class User():
    name = "User"
    health = 100
    damage = 10
    type_damage = "iron sword"
    
    def __str__(self):
        result = f"{self.name} имеет: {self.health}  единиц здоровья, {self.damage} единиц атаки. Тип атаки: {self.type_damage}"
        return result

class Magician(User):
    name = "Magician"
    health = 65
    damage = 30
    type_damage = "Magic Wand"

   
class Warior(User):
    name = "Warior"
    health = 150
    damage = 20
    type_damage = "Big iron sword"


class Archer(User):
    name = "Archer"
    health = 50
    damage = 50
    type_damage = "Bow"
    

print(Archer())