from collections import deque

class Task05():
    def __init__(self):
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
        self.shortest_distance_calculator()

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
            
            #print(item_position)

        for item_init_input in self.items_init_input:
            coordinate = {
                'name': item_init_input[2],
                'item_position': { 'x': item_init_input[0], 'y': item_init_input[1] },                
                'receiving_position': direction_processor({ 'x': item_init_input[0], 'y': item_init_input[1] }, item_init_input[3])
            }        

            self.coordinates.append(coordinate)

        #print(self.coordinates)
    
    def shortest_distance_calculator(self): #BFSを用いて各商品間の最短距離を算出する
        self.distances_between_items = []
        queue = deque()
        visited_coordinates = []
        already_visited = False

        def collision_detector(position):
            if(position['y'] == 0): #マップ底辺
                return False
            
            if(position['y'] == self.coordinate_init_input[1] - 1): #マップ頂辺
                if(position['x'] == 0 or position['x'] == self.coordinate_init_input[0] - 1):
                    return False
                
            if(not 0 <= position['x'] <= self.coordinate_init_input[0] - 1): #マップを超えた場合(x)
                return False
            
            if(not 0 <= position['y'] <= self.coordinate_init_input[1] - 1): #マップを超えた場合(y)
                return False
            
            for coordinate in self.coordinates: #アイテムの位置と被るか
                if(position['x'] == coordinate['item_position']['x'] and position['y'] == coordinate['item_position']['y']):
                    return False
            
            return True
        
        def next_position_calculator(current_position):
            next_positions = [
                { 'x': current_position['x'], 'y': current_position['y'] + 1 },
                { 'x': current_position['x'] + 1, 'y': current_position['y'] },
                { 'x': current_position['x'], 'y': current_position['y'] - 1 },
                { 'x': current_position['x'] - 1, 'y': current_position['y'] }
            ]

            return next_positions                    
        
        for coordinate in self.coordinates:
            distance_between_items = []
            queue.append({ 'x': coordinate['receiving_position']['x'], 'y': coordinate['receiving_position']['y'], 'distance': 0 })
            visited_coordinates.append({ 'x': coordinate['receiving_position']['x'], 'y': coordinate['receiving_position']['y'], 'distance': 0 })

            while len(queue) > 0:
                current_position = queue.popleft()
                next_positions = next_position_calculator(current_position)
                current_distance = current_position['distance']
        
                for next_position in next_positions:
                    if(collision_detector(next_position)):
                        for visited_coordinate in visited_coordinates: #訪問済みであるかの確認
                            if(next_position['x'] == visited_coordinate['x'] and next_position['y'] == visited_coordinate['y']):
                                already_visited = True
                                break
                            else:
                                already_visited = False
                        
                        if(already_visited == False):                        
                            next_position['distance'] = current_distance + 1
                            visited_coordinates.append(next_position)
                            queue.append(next_position)                    
                    else:
                        continue

            for coordinate in self.coordinates:
                for visited_coordinate in visited_coordinates:
                    if(coordinate['receiving_position']['x'] == visited_coordinate['x'] and coordinate['receiving_position']['y'] == visited_coordinate['y']):
                        distance_between_items.append({ coordinate['name']: visited_coordinate['distance'] })

            self.distances_between_items.append({ coordinate['name']: distance_between_items })

        #print(self.distances_between_items)

Task05()  




    

        
