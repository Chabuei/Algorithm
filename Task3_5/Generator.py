import random
from collections import deque

class Generator:
    def __init__(self):
        self.free = 1
        self.not_free = 0                

        self.init_map() #マップサイズ → 商品数 → 商品 →　BFSでマップの有効性確認 の優先順序で初期化していく
        self.init_products()
        self.init_orders()

        while(self.valid_map_checker() == 0): #有効なマップが生成されるまで繰り返す
            self.init_map()
            self.init_products()
            self.init_orders()

        #self.show()
        
    def init_map(self):
        self.map_size_width = random.randint(4, 10) #本当は100まで
        self.map_size_height = random.randint(4, 10) 
        self.map = [[self.free for _ in range(self.map_size_width)] for _ in range(self.map_size_height)]
        self.number_of_accesible_positions = (self.map_size_width * self.map_size_height) - (6 + (self.map_size_width - 4))
        
        for i in range(self.map_size_height): #入れない場所の初期化
            for j in range(self.map_size_width):
                if ((i == 0 and j == 0) or (i == 0 and j == self.map_size_width - 1) or (i == self.map_size_height - 1)):
                    if(j == 1):
                        self.start_position = (i, j) #タプルは基本的に変更はできない
                        continue                       

                    if(j == self.map_size_width - 2):
                        self.goal_position = (i, j)
                        continue                                             
                        
                    self.map[i][j] = self.not_free

        self.map[self.start_position[0]][self.start_position[1]] = 'S'                       
        self.map[self.goal_position[0]][self.goal_position[1]] = 'G'

    def valid_position_checker_for_init_products(self, position_x, position_y, direction): #positionがはみ出ていないか or not_freeでないかを確認する
        applied_position_x = 0
        applied_position_y = 0
        self.anti_cases = [self.not_free, 'S', 'G']

        if(direction == 'N'):
            applied_position_x = position_x 
            applied_position_y = position_y - 1

        if(direction == 'E'):
            applied_position_x = position_x + 1 
            applied_position_y = position_y

        if(direction == 'S'):
            applied_position_x = position_x 
            applied_position_y = position_y + 1

        if(direction == 'W'):
            applied_position_x = position_x - 1 
            applied_position_y = position_y

        if((0 <= applied_position_x and applied_position_x <= self.map_size_height - 1) and (0 <= applied_position_y and applied_position_y <= self.map_size_width - 1) and not(self.map[applied_position_x][applied_position_y] in self.anti_cases)):
            if((self.map[position_x][position_y] == self.not_free or self.map[position_x][position_y] == 'S' or self.map[position_x][position_y] == 'G') or (self.map[applied_position_x][applied_position_y] == self.not_free or self.map[position_x][position_y] == 'S' or self.map[position_x][position_y] == 'G')):
                return 0
            else:
                return 1
        else:
            return 0
        
    def position_calculator_from_direction(self, position_x, position_y, direction):
        if(direction == 'N'):
            return (position_x, position_y - 1)
        
        if(direction == 'E'):
            return (position_x + 1, position_y)
        
        if(direction == 'S'):
            return (position_x, position_y + 1)
        
        if(direction == 'W'):
            return (position_x - 1, position_y)

    def init_products(self):
        self.directions = ['N', 'E', 'S', 'W']
        self.number_of_products = random.randint(1, self.number_of_accesible_positions if self.number_of_accesible_positions <= 10 else 10) #本当は20まで
        self.list_of_products = []
        self.start_value = { 'name': 'S', 'position': self.start_position, 'accesible_position': (self.start_position[0], self.start_position[1] - 1), 'direction': 'N'}
        self.goal_value = { 'name': 'G', 'position': self.goal_position, 'accesible_position': (self.goal_position[0], self.goal_position[1] - 1), 'direction': 'N'}

        for i in range(self.number_of_products): #商品の初期化                        
            count = 0
            threshold = 10000             
            position_x = 0
            position_y = 0
            direction = self.directions[random.randint(0, 3)]            

            while(self.valid_position_checker_for_init_products(position_x, position_y, direction) == 0): #どこにも置けない場合無限ループになってしまうので閾値でループ回数を制限する
                if(count > threshold):
                    break                

                direction = self.directions[random.randint(0, 3)]
                position_x = random.randint(0, self.map_size_height - 1)
                position_y = random.randint(0, self.map_size_width - 1)

                count += 1
            
            accesible_position = self.position_calculator_from_direction(position_x, position_y, direction)
            self.map[position_x][position_y] = self.not_free
            #self.map[accesible_position[0]][accesible_position[1]] = self.not_free
            self.list_of_products.append({'name': str(i), 'position': (position_x, position_y), 'accesible_position': accesible_position, 'direction': direction})

        #print(self.list_of_products)

    def init_orders(self):
        self.number_of_orders = random.randint(1, len(self.list_of_products))
        self.list_of_orders = []
        
        for _ in range(self.number_of_orders):
            number_of_order = random.randint(1, len(self.list_of_products))
            list_of_order = random.sample(self.list_of_products, number_of_order)
            self.list_of_orders.append(list_of_order)

        #print(self.list_of_orders)

    def valid_position_checker_for_valid_map_checker(self, position_x, position_y):

        if((0 <= position_x and position_x <= self.map_size_height - 1) and (0 <= position_y and position_y <= self.map_size_width - 1)):
            if(self.map[position_x][position_y] == self.free):
                return 1
            else:
                return 0
        else:
            return 0
            

    def valid_map_checker(self): #bfsを用いてマップの有効性(全ての商品に対して、それらを獲得できるようなパスが必ず一つ存在する)を確認する
        queue = deque() #スタート側から
        count = 0
        visited = []
        valid_condition = (self.map_size_width * (self.map_size_height - 1)) - self.number_of_products
        
        queue.append(self.start_position)
        visited.append(self.start_position)

        while len(queue) > 0:
            current_position = queue.popleft()
            next_positions = [
                (current_position[0], current_position[1] - 1),
                (current_position[0] + 1, current_position[1]),
                (current_position[0], current_position[1] + 1),
                (current_position[0] - 1, current_position[1])
            ]

            for next_position in next_positions:
                if(self.valid_position_checker_for_valid_map_checker(next_position[0], next_position[1]) == 1):
                    if(not (next_position in visited)):
                        visited.append(next_position)
                        queue.append(next_position)
                        count += 1
                else:
                    continue

        queue2 = deque() #ゴール側から
        count2 = 0
        visited2 = []
        
        queue2.append(self.goal_position)
        visited2.append(self.goal_position)

        while len(queue2) > 0:
            current_position2 = queue2.popleft()
            next_positions2 = [
                (current_position2[0], current_position2[1] - 1),
                (current_position2[0] + 1, current_position2[1]),
                (current_position2[0], current_position2[1] + 1),
                (current_position2[0] - 1, current_position2[1])
            ]

            for next_position2 in next_positions2:
                if(self.valid_position_checker_for_valid_map_checker(next_position2[0], next_position2[1]) == 1):
                    if(not (next_position2 in visited2)):
                        visited2.append(next_position2)
                        queue2.append(next_position2)
                        count2 += 1
                else:
                    continue

        if((len(visited) + 1 == valid_condition) and (count == count2)):
            return 1
        else:
            return 0


            