import random
import itertools
from collections import deque
from Generator import Generator

class Solver:
    def __init__(self):
        self.generator = Generator()
        self.distance_calculator_between_products()
        self.n_opt()
        self.show()
        
    def distance_calculator_between_products(self):
        self.distances_between_products = []
        self.new_distances_between_products = []

        list_for_permutations = list(range(self.generator.number_of_products))
        list_for_permutations.append('S')
        list_for_permutations.append('G')
        self.combinations_of_products = list(itertools.permutations(list_for_permutations, 2))

        queue = deque()
        visited = []

        for combination in self.combinations_of_products:
            distance_map = [[0 for _ in range(self.generator.map_size_width)] for _ in range(self.generator.map_size_height)]
            queue.clear()
            visited = []
            start = {}
            goal = {}
            count = 0

            for i in range(2): #S Gの例外処理
                if (combination[i] == 'S' or combination[i] == 'G'):
                    if(i == 0):
                        start = self.generator.start_value
                    else:
                        goal = self.generator.goal_value
                else:
                    if(i == 0):
                        start = self.generator.list_of_products[combination[0]]
                    else:
                        goal = self.generator.list_of_products[combination[1]]

            queue.append(start['accesible_position'])
            visited.append(start['accesible_position'])

            while len(queue) > 0:
                current_position = queue.popleft()
                next_positions = [
                    (current_position[0], current_position[1] - 1),
                    (current_position[0] + 1, current_position[1]),
                    (current_position[0], current_position[1] + 1),
                    (current_position[0] - 1, current_position[1])
                ]

                for next_position in next_positions:
                    if(next_position == goal['accesible_position']):
                        self.distances_between_products.append({
                            'name': f'{combination[0]}→{combination[1]}', #商品aから商品bまでの距離
                            'distance': distance_map[current_position[0]][current_position[1]]
                        })
                    else:                                        
                        if(self.generator.valid_position_checker_for_valid_map_checker(next_position[0], next_position[1]) == 1):                        
                            distance_map[next_position[0]][next_position[1]] = distance_map[current_position[0]][current_position[1]] + 1

                            if(not (next_position in visited)):                            
                                visited.append(next_position)
                                queue.append(next_position)
                                count += 1                                                             
                        else:
                            continue

        for combination in self.combinations_of_products:
            temporal_list = []

            for distance in self.distances_between_products:
                if(distance['name'] == f'{combination[0]}→{combination[1]}'):
                    temporal_list.append(distance['distance'])

            self.new_distances_between_products.append({
                'name': f'{combination[0]}→{combination[1]}',
                'distance': min(temporal_list)
            })
                    
        #print(self.new_distances_between_products)
        #print()

    def total_distance_calculator(self, order): #引数に任意のオーダーを取り、その総距離を計算する
        total_distance = 0
        current_position = order[0]
        next_position = order[1]

        for i in range(len(order)):            
            for distance_between_products in self.distances_between_products:
                if (distance_between_products['name'] == f'{ current_position }→{ next_position }'):
                    total_distance += distance_between_products['distance']
                
            if(i + 2 <= len(order) - 1):
                current_position = order[i + 1]
                next_position = order[i + 2]
            else:
                break

        return total_distance

    def n_opt(self): #ここで各商品オーダーについて、n-opt近傍を適用する
        n = 2 #n個のオーダーを取る経路を入れ替える(n = 2の時、2-opt近傍という(nは多いほうがより最適解に近づくが、計算量は増える))
        threshold = 1000 #何回n-opt近傍を適用させるかを表す(数が多いほど最適解に近づく)        
        self.total_distances_of_orders = []        

        for i in range(len(self.generator.list_of_orders)): #一つ一つのオーダーについて
            count = 0
            current_order = []
            for j in range(len(self.generator.list_of_orders[i])):
                current_order.append(self.generator.list_of_orders[i][j]['name'])
            list_valid_indexes = list(range(1, len(current_order) + 1))
            current_order.insert(0, 'S')
            current_order.append('G')
        
            if(len(current_order) - 2 >= 2):
                for _ in range(threshold):                    
                    swapped_indexes = []
                    while True:
                        swapped_indexes = random.sample(list_valid_indexes, n)
                        if(not(0 in swapped_indexes and len(current_order) + 1)):
                            break                    

                    tmp_order = current_order[:] #参照渡しにならないよう注意                    
                    tmp_order[swapped_indexes[0]] = current_order[swapped_indexes[1]]
                    tmp_order[swapped_indexes[1]] = current_order[swapped_indexes[0]]
                    if(self.total_distance_calculator(tmp_order) < self.total_distance_calculator(current_order)):
                        current_order = tmp_order
                        print(f'Step: {count}, Current optimized distance of the order No.{i}: {self.total_distance_calculator(current_order)}')
                        count += 1
                    else:
                        current_order = current_order
                        count += 1
                self.total_distances_of_orders.append(self.total_distance_calculator(current_order))
            else:
                self.total_distances_of_orders.append(self.total_distance_calculator(current_order))
            print()

    def show(self):
        print(f'Width: {self.generator.map_size_width}, Height: {self.generator.map_size_height}, Number of products: {self.generator.number_of_products}')
        print()

        print('Produsts list')
        for i in range(len(self.generator.list_of_products)):
            print(f'position: ({self.generator.list_of_products[i]["position"]}), accesible_position: ({self.generator.list_of_products[i]["accesible_position"]}), name: {self.generator.list_of_products[i]["name"]}, direction: {self.generator.list_of_products[i]["direction"]}')
        print()

        print(f'Number of orders: {self.generator.number_of_orders}')
        print()

        for i in range(len(self.generator.list_of_orders)):
            for j in range(len(self.generator.list_of_orders[i])):
                print(self.generator.list_of_orders[i][j]['name'], end = ', ')
            print()
        print()            

        for i in range(self.generator.map_size_height):
            for j in range(self.generator.map_size_width):
                count = 0
                for k in range(len(self.generator.list_of_products)):
                    if((i, j) == self.generator.list_of_products[k]['position']):                                                
                        if(self.generator.list_of_products[k]['direction'] == 'N'):
                            print(f'↑[{self.generator.list_of_products[k]["name"]}]', end = ' ')
                            count += 1
                        if(self.generator.list_of_products[k]['direction'] == 'E'):
                            print(f'→[{self.generator.list_of_products[k]["name"]}]', end = ' ')
                            count += 1
                        if(self.generator.list_of_products[k]['direction'] == 'S'):
                            print(f'↓[{self.generator.list_of_products[k]["name"]}]', end = ' ')
                            count += 1
                        if(self.generator.list_of_products[k]['direction'] == 'W'):
                            print(f'←[{self.generator.list_of_products[k]["name"]}]', end = ' ')
                            count += 1                    
                if(count == 0):
                    print(f'  {self.generator.map[i][j]}', end = '  ')
            print()
        print()

        print('The optimized distances for each order')
        for i in range(len(self.total_distances_of_orders)):
            print(self.total_distances_of_orders[i], end = ', ')
                
Solver()
        