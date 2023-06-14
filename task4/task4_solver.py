# Solver for task2 and task4
# Implemented by Shingo Morimoto

class Task2_Solver(object):
    items = []
    queries = []
    combinations = []
    pair_dict= {}
    input_lines = []
    result = []

    def __init__(self) -> None:
        pass

    def solve(self):
        self.readInput()
        self.items = sorted(self.items)
        self.combinations = self.createCombinations(self.items)
        self.craetePairDict()
        self.count()
        self.sortByCount()
        # self.display(queries=self.queries)


    def readInput(self):
        N = int(input())

        for _ in range(N):
            input_list = input().split()
            input_list.pop(0)  # pop the number of products.

            self.input_lines.append(input_list) # 

            for product in input_list:
                if product not in self.items:
                    self.items.append(product)

        Q = int(input())
        for _ in range(Q):
            a, b = map(int, input().split())
            self.queries.append((a,b))


    def createCombinations(self, sorted_list):
        combinations = []
        for i, p1 in enumerate(sorted_list[:-1]):
            for p2 in sorted_list[i+1:]:
                pair = p1 + " " + p2
                combinations.append(pair)
        return combinations
    

    def craetePairDict(self):
        for pair in self.combinations:
            self.pair_dict[pair] = 0

    ### Inspect input lines and count co-occurence of two pairs ###
    def count(self):
        for purchased_items in self.input_lines:
            purchased_items = sorted(purchased_items)
            combinationsinLine = self.createCombinations(purchased_items)

            for conbi in combinationsinLine:
                self.pair_dict[conbi] += 1


    def sortByCount(self):
        sorted_pair_list_by_value = sorted(self.pair_dict.items(), key=lambda x:x[1], reverse=True)
        self.result = sorted_pair_list_by_value




    def display(self):

        for first, second in self.queries:
            lower = first-1
            upper = second-1

            # print(f'({first}, {second})')

            for d in self.result[lower:upper+1]:
                print(d[1], d[0])






if __name__ == '__main__':
    solver = Task2_Solver()
    solver.solve()
    solver.display()


    

    
