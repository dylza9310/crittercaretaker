# Critter Caretaker Module
# This module defines the Critter class and its methods for managing critters.

def plantSeed(initial_state="seed"):
        print("///////////")
        print("///--O--///")
        print("///////////")

class PlantCritter(object):
    """A virtual pet"""
    
    def initialize(self):
        import time
        print("Planting...")
        time.sleep(2)
        print("Your plant is now ready to be cared for!")
        plantSeed()
    


#Main
pcrit = PlantCritter()
pcrit.initialize()
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
