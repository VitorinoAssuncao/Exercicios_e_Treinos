from random import randint
from templates.creatures.undeads import Undeads

undeads = Undeads()

def rng_battle_cemitery():
    battle = randint(1,10)
    enemy = Undeads()
    if battle >= 1 and battle <= 3:
        enemy = undeads.create_zombie(1)
    elif battle >= 4 and battle <= 8:
        enemy = undeads.create_zombie(1)
    elif battle == 9:
        enemy = undeads.create_shadow(1)
    else:
        enemy = undeads.create_shadow(3)
    print(f'Specie:{enemy._species} \n Level: {enemy._lv} \n HP:{enemy._hp}')
    return enemy