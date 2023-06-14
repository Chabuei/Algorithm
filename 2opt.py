import random

class Task05():
    def __init__(self):
        """ 
        self.coordinate_init_input = [8, 8, 14] #Task03のExampleバージョン

        self.items_init_input = [     
            [0, 1, 'a', 'E'],
            [0, 2, 'b', 'E'],
            [0, 3, 'c', 'E'],
            [0, 4, 'd', 'E'],
            [1, 7, 'e', 'S'],
            [3, 7, 'f', 'S'],
            [6, 7, 'g', 'S'],
            [7, 5, 'h', 'W'],
            [7, 1, 'i', 'W'],
            [3, 4, 'j', 'W'],
            [3, 3, 'k', 'W'],
            [3, 2, 'l', 'W'],
            [4, 4, 'm', 'N'],
            [4, 3, 'n', 'S']
        ]

        self.order_init_input = 4

        self.orders_init_input = [
            [4, 'a', 'b', 'c', 'd'],
            [3, 'a', 'e', 'g'],
            [4, 'b', 'j', 'n', 'g'],
            [14, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        ]
        """

        self.coordinate_init_input = [5, 5, 4] #Task03のExampleの簡易バージョン

        self.items_init_input = [     
            [0, 1, 'a', 'E'],
            [2, 2, 'b', 'W'],
            [1, 4, 'c', 'S'],
            [4, 2, 'd', 'W'],
        ]

        self.order_init_input = 1

        self.orders_init_input = [
            [4, 'a', 'b', 'c', 'd']            
        ]

        self.data_processor()
        self.shortest_path_calculator()
        self.show()

    def data_processor(self):
        self.coordinates = []

        def direction_processor(item_position, direction):
            if(direction == 'N'):
                return { 'x': item_position['x'], 'y': item_position['y'] + 1 }
            
            if(direction == 'E'):
                return { 'x': item_position['x'] + 1, 'y': item_position['y'] }
            
            if(direction == 'S'):
                return { 'x': item_position['x'], 'y': item_position['y'] - 1 }
            
            if(direction == 'W'):
                return { 'x': item_position['x'] - 1, 'y': item_position['y'] }
            
            print(item_position)

        for item_init_input in self.items_init_input:
            coordinate = {
                'name': item_init_input[2],
                'item_position': { 'x': item_init_input[0], 'y': item_init_input[1] },                
                'receiving_position': direction_processor({ 'x': item_init_input[0], 'y': item_init_input[1] }, item_init_input[3])
            }        

            self.coordinates.append(coordinate)

        #print(self.coordinates)
    
    def shortest_distance_calculator(self): #BFSを用いて各商品間の最短距離を算出する
        #あとでBFSで実装する
        None

    def shortest_path_calculator(self): #3-opt近傍を用いて最短経路の近似解を算出する
        self.next_available_positions = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.shortest_distance = {
            'a': { 'b': 1, 'c': 2, 'd': 3 },
            'b': { 'a': 1, 'c': 1, 'd': 4 },
            'c': { 'a': 2, 'b': 1, 'd': 3 },
            'd': { 'a': 3, 'b': 4, 'c': 3 }
        }        

        self.nodes = ['a', 'b', 'c', 'd']
        self.current_path = ['a', 'c', 'd', 'b'] #経路の初期化
        self.array_elements = [0, 1, 2, 3]

        self.side1 = [self.current_path[0], self.current_path[1]]
        self.side2 = [self.current_path[1], self.current_path[2]]
        self.side3 = [self.current_path[2], self.current_path[3]]

        self.sum_distance = self.shortest_distance[self.side1[0]][self.side1[1]] + self.shortest_distance[self.side2[0]][self.side2[1]] + self.shortest_distance[self.side3[0]][self.side3[1]] 
            
        for i in range(100):
            random_array = random.sample(self.array_elements, 4)
            temporal_path = [self.current_path[random_array[0]], self.current_path[random_array[1]], self.current_path[random_array[2]], self.current_path[random_array[3]]]

            temporal_side1 = [temporal_path[0], temporal_path[1]]
            temporal_side2 = [temporal_path[1], temporal_path[2]]
            temporal_side3 = [temporal_path[2], temporal_path[3]]

            temporal_sum_distance = self.shortest_distance[temporal_side1[0]][temporal_side1[1]] + self.shortest_distance[temporal_side2[0]][temporal_side2[1]] + self.shortest_distance[temporal_side3[0]][temporal_side3[1]] 
            
            if(temporal_sum_distance < self.sum_distance):
                self.sum_distance = temporal_sum_distance
                
                for i in range(4):
                    self.current_path[i] = temporal_path[i]

        """
        def collide_detector(position):
            if(position['x'] > 5 or position['y'] > 5):
                return True

            #Xにぶつかていないか

            #商品にぶつかっていないかs 
        """

        """
        for i in range(self.coordinate_init_input[0]):
            for j in range(self.coordinate_init_input[1]):
        """

    def show(self):
        print('Shortest path is ' + self.current_path[0] +self.current_path[1] + self.current_path[2] + self.current_path[3])
        print('The total costs of the path is' + str(self.sum_distance))

Task05()  




    

        
