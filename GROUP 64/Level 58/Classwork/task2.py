class Tank:
    def __init__(self, name, role, armour):
        self.name = name
        self.role = role
        self.armour = armour


tank1 = Tank("Leopard 2A4", "MBT", "500-600mm")
tank2 = Tank("Bagleitpanzer", "Light tank", "100-150mm")
tank3 = Tank("Leopard 2K", "Medium tank", "300-400mm")

print("Name: ", tank2.name)
print("Role: ", tank2.role)
print("Armour: ", tank2.armour)
