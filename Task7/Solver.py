import random
import itertools
from collections import deque
from Generator import Generator

class Solver:
    def __init__(self):
        self.generator = Generator()
        self.distance_calculator_between_shelves()
        self.products_layouter()
        self.optimizer()
        self.show()
        
    def distance_calculator_between_shelves(self):
        self.distances_between_shelves = []
        self.new_distances_between_shelves = []

        list_for_permutations = list(range(self.generator.number_of_shelves))
        list_for_permutations.append('S')
        list_for_permutations.append('G')
        self.combinations_of_shelves = list(itertools.permutations(list_for_permutations, 2))

        queue = deque()
        visited = []

        for combination in self.combinations_of_shelves:
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
                        start = self.generator.list_of_shelves[combination[0]]
                    else:
                        goal = self.generator.list_of_shelves[combination[1]]

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
                        self.distances_between_shelves.append({
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

        for combination in self.combinations_of_shelves:
            temporal_list = []

            for distance in self.distances_between_shelves:
                if(distance['name'] == f'{combination[0]}→{combination[1]}'):
                    temporal_list.append(distance['distance'])

            self.new_distances_between_shelves.append({
                'name': f'{combination[0]}→{combination[1]}',
                'distance': min(temporal_list) if min(temporal_list) else 0
            })
                    
        #print(self.new_distances_between_shelves)
        #print()

    def total_distance_calculator(self, order): #引数に任意のオーダーを取り、その総距離を計算する
        total_distance = 0
        
        current_position = 'S'
        next_position = self.list_of_products[int(order[1])]['belong_to']['name']

        for i in range(len(order)):            
            for distance_between_shelves in self.distances_between_shelves: #距離データベース
                if (distance_between_shelves['name'] == f'{ current_position }→{ next_position }'):
                    total_distance += distance_between_shelves['distance']
                
            if(i + 2 <= len(order) - 1):
                if(order[i + 2] == 'G'):
                    current_position = self.list_of_products[int(order[i + 1])]['belong_to']['name']
                    next_position = 'G'
                else:
                    current_position = self.list_of_products[int(order[i + 1])]['belong_to']['name']
                    next_position = self.list_of_products[int(order[i + 2])]['belong_to']['name']
            else:
                break

        return total_distance

    def init_products(self):
        self.list_of_products = []

        for i in range(len(self.generator.list_of_shelves)):
            self.list_of_products.append({'name': str(i), 'belong_to': ''})

        #print(self.list_of_products)

    def products_layouter(self):
        self.init_products()
        next_shelves_selection = random.sample(self.generator.list_of_shelves, len(self.generator.list_of_shelves))
        for i in range(len(self.generator.list_of_shelves)):
            self.list_of_products[i]['belong_to'] = next_shelves_selection[i]

        #print(self.list_of_products)

    def optimizer(self): #ランダムでレイアウトを作り、もしそのレイアウトが高いスコアを得られた場合、レイアウトを更新する(ひたすらこれを繰り返すことで、ユーザの移動距離が最も少なくなるようなユーザにとっての理想的なレイアウトが実現できる)
        threshold = 5000
        self.worst_scenario = len(self.generator.list_of_orders) * self.generator.map_size_width * self.generator.map_size_height
        self.optimized_layout = []
        count = 0

        for _ in range(threshold):
            self.total_distances_of_orders = []
            sum_of_total_distances = 0
            self.products_layouter()
            for i in range(len(self.generator.list_of_orders)): #一つ一つのオーダーについて
                current_order = []                
                for j in range(len(self.generator.list_of_orders[i])):
                    current_order.append(self.generator.list_of_orders[i][j]['name'])
                current_order.insert(0, 'S')
                current_order.append('G')
                self.total_distances_of_orders.append(self.total_distance_calculator(current_order))     

            sum_of_total_distances = sum(self.total_distances_of_orders)
            if(sum_of_total_distances < self.worst_scenario):
                self.worst_scenario = sum_of_total_distances
                self.optimized_layout = self.list_of_products[:]
                print(f'Step:{count}, Current optimized the sum of total distances of users: {self.worst_scenario}')
                count += 1
            else:
                count += 1
        print()
                

    def show(self):
        print(f'Width: {self.generator.map_size_width}, Height: {self.generator.map_size_height}, Number of shelves: {self.generator.number_of_shelves}')
        print()

        print('Shelves list')
        for i in range(len(self.generator.list_of_shelves)):
            print(f'position: ({self.generator.list_of_shelves[i]["position"]}), accesible_position: ({self.generator.list_of_shelves[i]["accesible_position"]}), name: {self.generator.list_of_shelves[i]["name"]}, direction: {self.generator.list_of_shelves[i]["direction"]}')
        print()

        print(f'Number of products: {len(self.list_of_products)}')
        print('Products list')
        for i in range(len(self.list_of_products)):
            print(f'name: {self.list_of_products[i]["name"]}, belong to the shelve of : {self.list_of_products[i]["belong_to"]["name"]}')
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
                for k in range(len(self.generator.list_of_shelves)):
                    if((i, j) == self.generator.list_of_shelves[k]['position']):                                                
                        if(self.generator.list_of_shelves[k]['direction'] == 'N'):
                            print(f'↑[{self.generator.list_of_shelves[k]["name"]}]', end = ' ')
                            count += 1
                        if(self.generator.list_of_shelves[k]['direction'] == 'E'):
                            print(f'→[{self.generator.list_of_shelves[k]["name"]}]', end = ' ')
                            count += 1
                        if(self.generator.list_of_shelves[k]['direction'] == 'S'):
                            print(f'↓[{self.generator.list_of_shelves[k]["name"]}]', end = ' ')
                            count += 1
                        if(self.generator.list_of_shelves[k]['direction'] == 'W'):
                            print(f'←[{self.generator.list_of_shelves[k]["name"]}]', end = ' ')
                            count += 1                    
                if(count == 0):
                    print(f'  {self.generator.map[i][j]}', end = '  ')
            print()
        print()

        print(f'The sum of total distances of users: {self.worst_scenario}')
        print('Layouts of Products')
        for i in range(len(self.optimized_layout)):
            print(f'name: {self.optimized_layout[i]["name"]}, belong to the shelve of: {self.optimized_layout[i]["belong_to"]["name"]}')
        print()
                                        
Solver()
        