
class Combat_Mechanics():

    def calculate_dmg(self,atk_active,def_passive):
        if atk_active - def_passive == 0:
            return 0
        else:
            return atk_active - def_passive

    def actualize_hp(self,value_dmg,hp_initial):
        return hp_initial - value_dmg



    def combat_turn(self,player,enemy):
        turn = 1
        while player._hp > 0 or enemy._hp > 0:
            if turn % 2 == 0:
                option = input('Deseja atacar? 1- Sim, 2 - Não \n')
                if option == 1:
                    dmg = self.calculate_dmg(player._attack,enemy._defense) 
                    self.actualize_hp(dmg,enemy._hp)
            else:
                dmg = self.calculate_dmg(enemy._attack,player._defense) 
                self.actualize_hp(dmg,player._hp)