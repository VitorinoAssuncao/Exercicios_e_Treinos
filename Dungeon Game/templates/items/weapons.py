from random import randint

class Weapon():
    def __init__(self,name,min_dmg,max_dmg,durability):
        self._name = name
        self._min_dmg = min_dmg
        self._max_dmg = max_dmg
        self._durability = durability

    def roll_dmg(self):
        return randint(self._min_dmg,self._max_dmg)