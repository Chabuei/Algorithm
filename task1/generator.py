import random
import string
#============= configlations ================#
N = 6
Q = 2
NumItems = 40
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

print(N)


for i in range(N):
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


    print()

print(Q)

for i in range(Q):
    # 1 <= a <= 8 までの値を取得する
    a = random.randint(1, len(items))
    b = random.randint(a, len(items))
    print(a, end=" ")
    print(b, end=" ")
    print()
