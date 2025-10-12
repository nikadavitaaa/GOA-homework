class Fighter:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

    def heal(self, amount):
        self.health += amount
        print(f"{self.name}-ამ დაიჰილა {amount} სიცოცხლე. ახალი HP: {self.health}")

    def info(self):
        print(f"სახელი: {self.name}, სიცოცხლე: {self.health}, დემეიჯი: {self.damage}, სიჩქარე: {self.speed}")

class Archer(Fighter):
    def __init__(self, name, health, damage, speed, range, reload):
        super().__init__(name, health, damage, speed)
        self.range = range
        self.reload = reload

    def info(self):
        super().info()
        print(f"რეინჯი: {self.range}, გადატენვა: {self.reload}\n")

class Mage(Fighter):
    def __init__(self, name, health, damage, speed, spell, mana):
        super().__init__(name, health, damage, speed)
        self.spell = spell
        self.mana = mana

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.name}-მა გამოიყენა '{self.spell}', დარჩენილი მანა: {self.mana}")
        else:
            print(f"{self.name}-ს არ ეყო მანა.")

    def info(self):
        super().info()
        print(f"მაგია: {self.spell}, მანა: {self.mana}")

ninja = Archer("Ninja", 100, 25, 90, 15, 2)
samurai = Archer("Samurai", 120, 30, 80, 10, 3)
tribesman = Archer("Tribesman", 90, 20, 70, 18, 1)

viking = Mage("Viking", 130, 35, 75, "Thunder Strike", 40)
warrior = Mage("Warrior", 150, 40, 60, "Fireball", 50)
veteran = Mage("Veteran", 110, 28, 65, "Healing Aura", 35)
necromancer = Mage("Necromancer", 90, 20, 55, "Raise Dead", 100)

ninja.info()
viking.info()

viking.cast_spell()
necromancer.cast_spell()
ninja.heal(20)