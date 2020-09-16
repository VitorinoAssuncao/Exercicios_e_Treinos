class Player():
    def __init__(self,nome):
        self.__nome = nome
        self.__map = []
        self.__map_of_actions = []

    def get_name(self):
        return self.__nome

    def set_map(self,map):
        self.__map = map

    def get_map(self):
        return self.__map

    def set_map_of_actions(self,map_of_actions):
        self.__map_of_actions = map_of_actions

    def get_map_of_actions(self):
        return self.__map_of_actions