# You're a pet lover and have different pets at home. Your sibling is visiting you and they can't remember the names of your pets. Finish the Pet class to help your sibling associate a pet's name with its properties, like its family or color. 
# 1. Within the Pet class, create instance variables name, family, animal_type, and color to store the specific information received in the parameters. 

class Pet:
    def __init__(self, name, family, animal_type, color):
        self.name = name
        self.family = family
        self.animal_type = animal_type
        self.color = color

rio = Pet("Rio", "Macaw", "Parrot", "Blue")
coco = Pet("Coco", "Poodle", "Dog", "White")
bud = Pet("Bud", "Labrador", "Dog", "Brown")
daisy = Pet("Daisy", "Burmese", "Cat", "Grey")

print (f"{rio.name} is a {rio.color} colored {rio.family} {rio.animal_type}")