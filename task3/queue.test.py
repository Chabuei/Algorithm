# from collections import deque

from solver import Point
from solver import Item
# queue = deque([Point(4, 5), Point(5, 6), Point(2, 3)])
# queue.append(Point(1, 2))
# print(queue.popleft())
# print(queue.pop())
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

clockwise = True

if clockwise == True:
    DIRECTIONS = reversed(DIRECTIONS)

# for dx, dy in DIRECTIONS:
#     print(dx, dy)

# print(DIRECTIONS)
visiting_order = self.items.copy()# list of N items

for item in visiting_order:
    print(item)
