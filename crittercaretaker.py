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
    unhappiness = self.water + self.boredom
    if unhappiness < 5:
        return "Your plant is thriving!"
    elif 5 <= unhappiness < 10:
        return "Your plant is doing okay, but could use some care."
    elif 10 <= unhappiness < 15:
        return "Your plant is unhappy and needs attention!"
    


class PlantCritter(object):
    """A virtual pet"""
    
    def initialize(self, name, water=0, boredom=0):
        import time
        print("Planting...")
        time.sleep(2)
        print("Your plant is now ready to be cared for!")
        plantSeed()
        self.name = name # public attribute
        self.water = water # public attribute
        self.boredom = boredom # public attribute


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

    def play_with_plant(self, fun= 4):
        print("Your plant is playing with you!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
    
    
        
     

#Main
def main():
    pcrit_name = input("What would you like to name your plant? ")
    crit = PlantCritter(pcrit_name)

    choice = None
    while choice != "0":
        print("""
        Plant Caretaker Module
        0 - Exit
        1 - Water the plant
        2 - Play with the plant
        3 - Check plant status
        4 - Check plant mood
        """)
        
        choice = input("Choice: ")
        
        if choice == "1":
            crit.water_plant()
            print(crit.__stats__())
        elif choice == "2":
            crit.play_with_plant()
            print(crit.__stats__())
        elif choice == "3":
            print(crit.__stats__())
        elif choice == "4":
            print(crit.mood())
        else: choice == "0":


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
