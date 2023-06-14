"""
Usage: python solver.py < input.txt
"""

from collections import deque

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        str = f'({self.x}, {self.y})'
        return str

    # This function calcurate neighbor's location and return as Point Object.
    #   input : 'E' or 'W' or 'S' or 'N'
    def addDirction(self, DIR): 
        if DIR == 'E':
            dx = 1
            dy = 0
        elif DIR == 'W':
            dx = -1
            dy = 0
        elif DIR == 'N':
            dx = 0
            dy = 1        
        elif DIR == 'S':
            dx = 0
            dy =-1         
        else:
            dx = 0
            dy = 0        
        return Point(self.x + dx, self.y + dy)
            
INF = 99999999999999

class Item():

    distanceFromENTRANCE = INF  # distance from Entrance to it's targetPoint
    distanceFromEXIT = INF      # distance from Exit to it's targetPoint
    def __init__(self, x, y, name, direction, solver):
        self.point = Point(x, y)
        self.name = name
        self.direction = direction
        # Point object of location where the costmer can take this item.
        self.targetPoint = self.point.addDirction(self.direction) 
        
        solver.target.append(self.targetPoint)
        solver.stopFields.append(self.point)
        

    def __str__(self):
        str = f' {self.point.__str__()}, {self.name}, {self.direction} : target={self.targetPoint.__str__()}'
        return str
    
class Task3_solver:
    W = None
    H = None
    N = None
    ENTRANCE = None
    EXIT = None
    stopFields = []  # ここに、踏み込めない場所 を格納　全てPoint 型
    items = []
    target = []

    def __init__(self):
        pass

    def readInput(self):
        ### Read input data from input.txt ###
        W, H, N = map(int, input().split())
        self.W, self.H, self.N = W, H, N
        self.ENTRANCE = Point(1, 0)
        self.EXIT = Point(W-2, 0)

        # stopFields
        self.stopFields.append(self.ENTRANCE)
        self.stopFields.append(Point(0, 0))
        self.stopFields.append(Point(W-1, 0))
        self.stopFields.append(Point(0, H-1))
        self.stopFields.append(Point(W-1, H-1))
        for x in range(2, W-2):
            self.stopFields.append(Point(x, 0))


        
        for _ in range(N):
            x, y, name, direction = input().split()
            x = int(x)
            y = int(y)
            self.items.append(Item(x, y, name, direction, self))

    def print(self):
        # Print out every item and it's target point
        for item in self.items:
            print(item)
        pass

    def printStopFields(self):
        for p in self.stopFields:
            print(p)


    def printTargetFields(self):
        for p in self.target:
            print(p)

    '''
    This function returns the Minimum steps of route from point1 to point2 refering to it's stopFields and W, H
    if clockwise is True, search  clockwise
    else, search counter-clockwise
    '''
    # @classmethod
    # def bfs(self, point1, point2, clockwise):
    #     intx = 5
    #     return intx

    def is_valid(self, point):
        return 0 <= point.x < self.W and 0 <= point.y < self.H

    def bfs(self, start_P, goal_P, clockwise):
        DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if clockwise is False:
            DIRECTIONS = reversed(DIRECTIONS)

        visited = [[False for _ in range(self.W)] for _ in range(self.H)]  # mapping にしても良い
        distance = [[INF for _ in range(self.W)] for _ in range(self.H)]
        queue = deque([start_P])

        visited[start_P.y][start_P.x] = True
        distance[start_P.y][start_P.x] = 0

        while queue:
            current_P = queue.popleft()

            for dx, dy in DIRECTIONS:
                new_x = current_P.x + dx
                new_y = current_P.y + dy
                newPoint = Point(new_x, new_y)
                
                if newPoint.x == goal_P.x and newPoint.y == goal_P.y:
                    distance[new_y][new_x] = distance[current_P.y][current_P.x] + 1
                    return distance[new_y][new_x]
                if self.is_valid(newPoint) and not visited[new_y][new_x] and newPoint not in self.stopFields:
                    queue.append(Point(new_x, new_y))
                    visited[new_y][new_x] = True
                    distance[new_y][new_x] = distance[current_P.y][current_P.x] + 1

        # return distance
        return INF
    
    def calcDistancesFromEntrance(self):
        for item in self.items:
            item.distanceFromENTRANCE = self.bfs(self.ENTRANCE, item.targetPoint, clockwise=True)

    def calcDistancesFromExit(self):
        for item in self.items:
            item.distanceFromEXIT = self.bfs( item.targetPoint, self.EXIT, clockwise=True) # なぜかFalse だとうまくいかない

    '''
    This function returns the route by list of Items

    '''
    def solveRoute(self):
        route = [] 
        self.calcDistancesFromEntrance() 
        self.calcDistancesFromExit()     

        for item in self.items:
            dist_en = item.distanceFromENTRANCE
            if dist_en == INF:
                # There is an unreachable item.
                print("Error: Unreachable items found", item.name)
                return 
            
        for item in self.items:
            dist_ex = item.distanceFromEXIT
            if dist_ex == INF:
                # There is an unreachable item.
                print("Error: Unreachable items found", item.name)
                return 

        #### create route ####

        # for item in self.items:
            # print("Item:", item.name)
            # # print(f'Distance from EN: {item.distanceFromENTRANCE}, Distance from EX: {item.distanceFromEXIT}' )
            # print("EN-EX: ",item.distanceFromENTRANCE- item.distanceFromEXIT)
            # print("-----------------------------------------------------------")

        visiting_order = sorted(self.items, key = lambda item: item.name)  # ダミーの配列
        appended = []

        order_from_EX = sorted(self.items, key = lambda item :item.distanceFromEXIT)
        order_from_EN = sorted(self.items, key = lambda item :item.distanceFromENTRANCE)

        i = 0
        j = 0
        k = 0
   
        while len(appended) != self.N:
                
            while order_from_EN[i] in appended:
                i += 1
            visiting_order[k] = order_from_EN[i]
            appended.append( order_from_EN[i])

            print("append", appended[-1].name , "前から")

            if len(appended) == self.N: 
                break

            while order_from_EX[j] in appended:
                j += 1

            visiting_order[-k-1] = order_from_EX[j]
            appended.append(order_from_EX[j])
            print("append", appended[-1].name  , "後ろから")
            k += 1

        print("*"*20)
        for item in appended:
            print(item.name)
        # Sort
        # self.items = sorted(self.items, key = lambda item :(item.distanceFromENTRANCE+ item.distanceFromEXIT) )


        print("\n")
        print("="*20+"After Sorting"+"="*20)
        print("\n")

        for item in visiting_order:
            print("Item:", item.name)
            # print(f'Distance from EN: {item.distanceFromENTRANCE}, Distance from EX: {item.distanceFromEXIT}' )
            # print("EN-EX: ",item.distanceFromENTRANCE- item.distanceFromEXIT)
            print("-----------------------------------------------------------")

        # # self.print()
        # pass
        


def sort_key(item):
    if (item.distanceFromENTRANCE- item.distanceFromEXIT) < 0:
        return item.distanceFromENTRANCE
    elif (item.distanceFromENTRANCE- item.distanceFromEXIT) > 0:
        return -item.distanceFromEXIT
    
    else:
        return item.distanceFromENTRANCE

if __name__ == '__main__':
    # main()

    solver = Task3_solver()
    solver.readInput()
    # solver.print()
    # solver.printStopFields()
    # solver.printTargetFields()
    solver.solveRoute()
