# Critter Caretaker Module
# This module defines the Critter class and its methods for managing critters.
  

def plantSeed(self):
    evolution = self.happiness
    if  evolution > 0:
        print("///////////")
        print("///--O--///")
        print("///////////\n")
    elif  evolution > 100:
        print("     |     ")
        print("///--O--///")
        print("///////////")
        print("///////////\n")
    elif evolution > 200:
        print("     |     ")
        print("     |     ")
        print("///--O--///")
        print("///////////\n")
    elif evolution > 300:
        print("   // \\    ")
        print("  -- o --   ")
        print("   \\|//    ")
        print("     |      ")
        print("///-/-\-///")
        print("///////////\n")

def mood(self):
    unhappiness = self.water + self.happiness
    if unhappiness < 5:
        return "Your plant is thriving!"
    elif 5 <= unhappiness < 10:
        return "Your plant is doing okay, but could use some care."
    elif 10 <= unhappiness < 15:
        return "Your plant is unhappy and needs attention!"
    


class PlantCritter(object):
    """A virtual pet"""
    
    def initialize(self, name, water=0, happiness=10):
        import time
        print("Planting...")
        time.sleep(2)
        print("Your plant is now ready to be cared for!")
        plantSeed()
        self.name = name # public attribute
        self.water = water # public attribute
        self.happiness = happiness # public attribute


    def __stats__(self):
        rep = "Plant critter object\n"
        rep += "- Name:" + self.name + "\n"
        return rep
        
    
    def __pass_time(self):
        self.water += 1
        self.happiness -= 1

    def water_plant(self, food= 4):
        print("Glug glug... Your plant has been watered.")
        self.water -= food
        if self.water < 0:
            self.water = 0
        self.__pass_time()
    
    
        
     

#Main
pcrit = PlantCritter()
pcrit.initialize("Fernie")
print(pcrit)
print(pcrit.mood)

input("\n\nPress enter to exit.")


#Plant Caretaker Module
#1. Define a class named Critter.
#2. Add a method named talk that prints a message.
#3. Abandon the talk method and replace it with an initialize method that simulates planting a plant.
#5. Introduce the feeding and playing methods.
#4. Rename to Plant Caretaker Module 
#6. Add a method to water the plant.
#7. Add a method to play with the plant.
#8. Add a method to clean the plant's pot.
#8. Implement a method to display the plant's status.
#9. Add a method to check if the plant needs water and is happy.
#10. Define threshold values for hunger and happiness.
#11. Add an evolution method that changes the critter's state based on care thresholds (early, mid, late phases).
