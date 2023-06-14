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

    def bfs(self, start_P, goal_P_list, clockwise):
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
                
                # if newPoint.x == goal_P.x and newPoint.y == goal_P.y:
                #     distance[new_y][new_x] = distance[current_P.y][current_P.x] + 1
                #     return distance[new_y][new_x]
                if self.is_valid(newPoint) and not visited[new_y][new_x] and newPoint not in self.stopFields:
                    queue.append(Point(new_x, new_y))
                    visited[new_y][new_x] = True
                    distance[new_y][new_x] = distance[current_P.y][current_P.x] + 1

            # result = []
        for goal_P in goal_P_list:
            dist = distance[goal_P.y][goal_P.x]
            print(f"From {start_P} To {goal_P} : {dist}", )


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


    # def solveRoute(self):
    def calcDistance(self):
        for item in self.items:
            print("Item ", item.name)
            self.bfs(item.targetPoint, self.target, clockwise=True)
            print("-"*28)




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
    # solver.solveRoute()
    solver.calcDistance()
