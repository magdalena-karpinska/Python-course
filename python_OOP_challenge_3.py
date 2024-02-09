# Castles can be made out of different materials, help us describe the class WoodCastle.
# 1. Create the appropriate method to desribe WoodCastle.


class Castle:
    def description(self):
        return "This is a generic castle."
    
class StoneCastle(Castle):
    def description(self):
        return "This is a stone castle."
    
class WoodCastle(Castle):
    def description(self):
        return "This is a wood castle."


stone_castle = StoneCastle()
stone_castle_description = stone_castle.description()
print(stone_castle_description)

wood_castle = WoodCastle()
wood_castle_description = wood_castle.description()
print(wood_castle_description)