from templates.creatures.monster import Monster

class Undeads():

    def create_zombie(self,lv):
        zombie = Monster('zombie',lv,10*lv,2*lv,1*lv,lv-1)
        return zombie

    def create_skeleton(self,lv):
        skeleton = Monster('skeleton',lv,5*lv,3*lv,1*lv,lv+1)
        return skeleton

    def create_shadow(self,lv):
        shadow = Monster('shadow',lv,1*lv,1*lv,3*lv,lv)
        return shadow