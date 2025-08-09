# Critter Caretaker Module
# This module defines the Critter class and its methods for managing critters.

class Critter(object)
    """A virtual pet"""
    def talk(self):
        print("Hi. I'm your pet critter.")

#Main
crit = Critter()
crit.talk()
input("\n\nPress enter to exit.")
