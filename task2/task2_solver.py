# Solver for task2 and task4
# Implemented by Shingo Morimoto
import random
import itertools

def main():
    items = []
    queries = []
    combinations = []
    pair_dict= {}
    input_lines = []

    N = int(input())

    for _ in range(N):
        input_list = input().split()
        input_list.pop(0)  # pop the number of products.

        input_lines.append(input_list) # 

        for product in input_list:
            if product not in items:
                items.append(product)

    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().split())
        queries.append((a,b))

    # print('------- Items ------')
    # print(items)
    # print('------- Queries ------')
    # print(queries)

########## Sort items ##################
    items = sorted(items)
    # print()
    # print('------- Sorted Items ------')
    # print(items)


### Make the list of 2-product pair
    # combinations = createCombinations(items)
    # print()
    # print('------- Combinations ------')
    # print(combinations)

### Make the dictionary 
    for pair in combinations:
        pair_dict[pair] = 0

    # print()
    # print('------- Pair dict ------')
    # print(pair_dict)
    # print("Num Of Items: ", len(items))
    # print("Combinations: ", len(combinations)) # Must be NumItems_C_2 == 10*9 / 2*1 if NumItesm = 10.

    print('\n------- Input Lines ------')
    for line in input_lines:
        print(line)

    ### Inspect input lines and count co-occurence of two pairs ###

    for purchased_items in input_lines:
        purchased_items = sorted(purchased_items)
        combinations = createCombinations(purchased_items)

        for conbi in combinations:
            pair_dict[conbi] += 1


    print('\n------- Pair dict ------')
    print(pair_dict)


    sorted_pair_list_by_value = sorted(pair_dict.items(), key=lambda x:x[1], reverse=True)

    print('\n------- Sorted list ------')
    for two in sorted_pair_list_by_value:
        print(two)

    
    ### Display reqested Information ###    

    print('\n------- Result ------')
    
    print()

    for first, second in queries:
        lower = first-1
        upper = second-1

        print(f'({first}, {second})')
        for d in sorted_pair_list_by_value[lower:upper+1]:
            print(d[1], d[0])



    



class Task2_Solver(object):
    items = []
    queries = []
    combinations = []
    pair_dict= {}
    input_lines = []
    result = []

    def __init__(self) -> None:
        self.readInput()
        self.items = sorted(self.items)
        self.combinations = self.createCombinations(self.items)
        self.craetePairDict()
        self.count()
        self.sortByCount()
        self.display(queries=self.queries)
        pass

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

    def display(self, queries):

        for first, second in queries:
            lower = first-1
            upper = second-1

            # print(f'({first}, {second})')

            for d in self.result[lower:upper+1]:
                print(d[1], d[0])




# def createCombinations(sorted_items):
#     combinations = []
#     for i, p1 in enumerate(sorted_items[:-1]):
#         for p2 in sorted_items[i+1:]:
#             pair = p1 + " " + p2
#             combinations.append(pair)
#     return combinations




if __name__ == '__main__':
    # main()
    solver = Task2_Solver()


    

    
