import random
options = ['scissors', 'rock', 'paper']
inputs = ['!exit', '!rating']

rating = 0
name = input()
print(f"Hello, {name}")
with open('rating.txt', 'r') as f:
    for line in f:
        if name in line:
            temp = line.split(' ')
            rating = int(temp[1])
            break
moves = input()

if moves != '':
    moves = moves.split(',')
    options = moves
print("Okay, let's start")
wins = {}
for el in options:
    j = options.index(el) + 1
    wins[el] = []
    for i in range(len(options) // 2):
        if j == len(options):
            j = 0
        wins[el].append(options[j])
        j += 1

while True:
    player = input()
    if player not in inputs and player not in options:
        print("Invalid input")
        continue
    elif player == '!exit':
        print("Bye!")
        break
    elif player == '!rating':
        print(f"Your rating: {rating}")
        continue
    computer = random.choice(options)

    if player == computer:
        win = 0
    elif computer in wins[player]:
        win = -1
    else:
        win = 1

    if win == -1:
        print(f"Sorry, but computer choose {computer}")
    elif win == 0:
        rating += 50
        print(f"There is a draw ({computer})")
    else:
        rating += 100
        print(f"Well done. Computer choose {computer} and failed")
