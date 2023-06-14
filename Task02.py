import random
import string

class Caluculator():
    def __init__(self): #ここではもりもとさんが作られたジェネレータ処理が行われます
        #============= configlations ================#
        N = random.randint(1, 100)
        Q = random.randint(1, 10)
        NumItems = 40

        self.N = N
        self.Q = Q
        self.user_items = []
        self.a = []
        self.b = []
        #============================================#

        items = [
            'tea', 
            'butter',
            'bread',
            'onion',
            'carrot',
            'potato',
            'rice',
            'water',
        ]

        # increase the variety of items to $(Numitems) types
        for i in range(NumItems-len(items)):
                # get a random string of 5 alphabets
                new_item = ''.join(random.choices(string.ascii_lowercase, k=5))
                items.append(new_item)

        # print(items)
        # print(len(items))
        ##########################################################################
        print('---input---')
        print(N)

        for i in range(N):
            user_input = []
            M = random.randint(1, 10) # (1<= M <= 10)

            print(M, end=" ")

            selectedRandoms = [] 

            while len(selectedRandoms) < M:

                randomN = random.randint(0, len(items)-1) # get randomNumber in 0<= n <= 7
                if not randomN in selectedRandoms:
                    selectedRandoms.append(randomN)
                
            # Now we have non-duplicated random numbers.

            for randomId in selectedRandoms:
                print(items[randomId], end=" ")
                user_input.append(items[randomId])
            
            self.user_items.append(user_input)
                
            print()

        print(Q)

        """
        for i in range(Q):
            # 1 <= a <= 8 までの値を取得する
            a = random.randint(1, len(items))
            b = random.randint(a, len(items)) bの最大値

            self.a.append(a)
            self.b.append(b)

            print(a, end=" ")
            print(b, end=" ")
            print() 
        """                  
    # (x, y, )
    def data_setter(self): #生成された単語とその出現回数を記録する辞書をセット
        self.item_dictionary = {} 

        for user_item in self.user_items:
            for item in user_item:
                if(not item in self.item_dictionary):
                    self.item_dictionary[item] = 1
                
                else:
                    self.item_dictionary[item] += 1

            # 先にアルファベット順でソート
        self.item_dictionary = {key: value for key, value in sorted(self.item_dictionary.items())}

    def sort(self): #self.data_setterで作られた辞書をソートする
        self.data_setter()  

        self.item_name_list = list(self.item_dictionary.keys())
        self.item_list = sorted(self.item_dictionary.items(), reverse = True, key = lambda x : x[1]) #sortedの戻り値はlist型

        for i in range(self.Q):
            # 1 <= a <= 8 までの値を取得する
            a = random.randint(1, len(self.item_list))
            b = random.randint(a, len(self.item_list))

            self.a.append(a)
            self.b.append(b)

            print(a, end=" ")
            print(b, end=" ")
            print()

        print('---input---')
        print('---output---')
        
    def display(self): #self.sortでソートされたリストをa,bの順位に応じて出力
        self.sort()

        for i in range(self.Q):
            for j in range(self.a[i], self.b[i] + 1):                
                print(self.item_list[j - 1])

        print('---output---')
        #print(self.item_list) self.item_listを見たい場合はこれを出力して順位が正しいか確認してみてください






if __name__ == '__main__':
    calculator = Caluculator()
    calculator.data_setter()
