# Critter Caretaker Module
# This module defines the Critter class and its methods for managing critters.
  

def plantSeed(self):
    evolution = self.water - self.boredom
    if  evolution == 0:
        print("///////////")
        print("///--O--///")
        print("///////////\n")
    elif  evolution >= 1 and evolution < 10:
        print("     |     ")
        print("///--O--///")
        print("///////////")
        print("///////////\n")
    elif evolution >= 11 and evolution <= 20:
        print("     |     ")
        print("     |     ")
        print("///--O--///")
        print("///////////\n")
    elif evolution >= 21:
        print("   // \\    ")
        print("  -- o --   ")
        print("   \\|//    ")
        print("     |      ")
        print("///-/-\-///")
        print("///////////\n")

class PlantCritter(object):
    """A virtual pet"""
    
    def __init__(self, name, water = 0, boredom = 0):
        self.name = name # public attribute
        self.water = water # public attribute
        self.boredom = boredom # public attribute
        
    def __pass_time(self):
        self.water += 3
        self.boredom -= 1.5

    def water_plant(self, food= 4):
        print("Glug glug... Your plant has been watered.")
        self.water += food
        if self.water < 0:
            self.water = 0
        self.__pass_time()
        print("Water Level: " + str(self.water))


    def play_with_plant(self, fun= 2):
        print("Your plant is playing with you!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
        print("Boredom Level: " + str(self.boredom + fun))

    def stats(self):
        print("Plant Name: " + self.name)
        print("Water Level: " + str(self.water))
        print("Boredom Level: " + str(self.boredom))
        print("Happiness Level: " + str(self.water - self.boredom))
    
    def mood(self):
        unhappiness = self.water + self.boredom
        if unhappiness < 5:
            print("Your plant is thriving!")
        elif 5 <= unhappiness < 10:
            print("Your plant is doing okay, but could use some care.")
        elif 10 <= unhappiness < 15:
            print("Your plant is unhappy and needs attention!")
    
    

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
        
        #Exit the program
        if choice == "0":
           print("Goodbye!")
        #Water the plant
        elif choice == "1":
           crit.water_plant()
        #Play with the plant
        elif choice == "2":
            crit.play_with_plant()
        #Check plant status
        elif choice == "3":
            crit.stats()
        #Check plant mood
        elif choice == "4":
            crit.mood() # Work in progress

        #Unknown choice
        else:
            print("Sorry, but", choice, "isn't a valid choice.")
        
        plantSeed(crit)


main()


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
