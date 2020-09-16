from templates.characthers.characther import Characther
from templates.items.weapons import Weapon

class Warrior(Characther):
    def __init__(self,name):
        super().__init__(name,'Warrior',1,10,2,1,1)
        self._weapon = Weapon('spear',2,4,10)

