from templates.characthers.characther import Characther
from templates.items.weapons import Weapon

class Rogue(Characther):
    def __init__(self,name):
        super().__init__(name,'Rogue',1,10,2,0,3)
        self._weapon = Weapon('dagger',1,2,10)

