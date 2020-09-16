from templates.characthers.characther import Characther
from templates.items.weapons import Weapon

class Knight(Characther):
    def __init__(self,name):
        super().__init__(name,'Knight',1,10,1,3,0)
        self._weapon = Weapon('sword',1,3,10)
