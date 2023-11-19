import os

os.system("")

class Character:
    def __init__(self,name,health,weapon):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = weapon

        
    def Attack(self,target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f'{self.name} dealt {self.weapon.damage} damage to {target.name}')
        
class Weapons:
    def __init__(self,name,weapon_type,damage,value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value
        
        
class Hero(Character):
    def __init__(self, name: str, health: int, weapon):
        super().__init__(name = name, health = health, weapon= weapon)
        
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color= 'green')
        
    def equip(self, weapon):
        self.weapon = weapon
        print(f'{self.name} equipped a (n) {self.weapon.name}')
        
    def drop(self):
        self.weapon = self.default_weapon
        print(f'{self.name} has dropped the {self.weapon.name}!')
        
class Enemy(Character):
    def __init__(self, name: str, health: int,weapon):
        super().__init__(name = name, health = health, weapon= weapon)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color= 'red')
        
class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"
                    }
    def __init__(self,entity,length: int = 20,is_colored = True,color = ''):
        self.length = length
        self.entity = entity
        self.max_value = entity.health_max
        self.currewnt_value = entity.health

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors['default']
        
    def update(self) -> None:
        self.current_value = self.entity.health
        
    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s HEALTH: {self.entity.health}/{self.entity.health_max}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")


#Objects weapons

iron_sword = Weapons(name = 'Iron Sword', weapon_type= 'sharp',damage= 5,value= 10)
short_bow = Weapons(name= 'shor bow', weapon_type= 'ranged', damage= 4, value= 8)
fists = Weapons(name= 'fist',weapon_type= 'blunt', damage= 2, value= 0)
# Objects Characters        
hero = Hero('Hero',100, fists)
enemy = Enemy('Enemy',100,short_bow)

while True:
    
    os.system('cls')
    
    
    hero.equip(iron_sword)
    hero.drop()

    hero.equip(iron_sword)
    hero.Attack(enemy)
    enemy.Attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()
    
    input()

    
