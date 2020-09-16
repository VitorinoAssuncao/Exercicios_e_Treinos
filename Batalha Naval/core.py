class Core_Rules():

    def define_water(self):
        return "|~~~|"

    def define_submarine(self,map,coord_x,coor_y):
        map[coord_x-1][coor_y-1] = " S "
        return map

    def try_to_shot(self,map,action_map,coord_x,coord_y):
        if map[coord_x-1][coord_y-1] == ' S ':
            map[coord_x-1][coord_y-1] = ' X '
            self.register_in_action_map(action_map,coord_x,coord_y,'S')
            print('OH YES!!! You hit this submarine')
        else:
            self.register_in_action_map(action_map,coord_x,coord_y,'W')
            print('Water!!!')
        return map

    def register_in_action_map(self,map,coord_x,coord_y,result):
        if result == 'S':
            map[coord_x-1][coord_y-1] = ' S '
        elif result == "W":
            map[coord_x-1][coord_y-1] = ' O '

    def count_submarines_alive(self,map):
        count_submarine = 0
        for i in range(0,len(map)):
            for x in range(0,len(map)):
                if map[i][x] == ' S ':
                    count_submarine += 1
        return count_submarine

    def create_map(self,size):
        new_map = []
        for i in range(0,size):
            new_line = []
            for x in range(0,size):
                new_line.append(self.define_water())
            new_map.append(new_line)
        return new_map

    def print_map(self,map):
        for count_line in range(0,len(map)):
            if count_line == 0:
                print(count_line,end=" ")
                for index_column in range(0,len(map)):
                    print(f"  {chr(index_column+65)}",end="   ")
                print("")
                print(count_line+1,end=" ")                
                for count_column in range(0,len(map[0])):
                    print(map[count_line][count_column],end=" ")
                print("")
            else:
                print(count_line+1,end=" ")                
                for count_column in range(0,len(map[0])):
                    print(map[count_line][count_column],end=" ")
                print("")