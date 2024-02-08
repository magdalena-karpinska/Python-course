# As a volunteer at the at a festival, you track the rides being installed. We have a class named Ride that stores the name of the ride and the suitable age group. Use instances of that class to track the rides installed today.
# 1. Create a new instance of the Ride class named roller_coaster and specify that its name Roller coaster and an adults ride. 
# 2. Create a new instance of the Ride class named ferris_wheel and specify that its name is Ferris wheel and a kids ride.

class Ride:
    def __init__(self, name, age_group):
        self.name = name
        self.age_group = age_group


roller_coaster = Ride("Roller coaster", "adults")
ferris_wheel = Ride ("Ferris wheel", "kids")


print(roller_coaster.age_group)
print(ferris_wheel.name)
