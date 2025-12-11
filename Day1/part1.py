import os

MAX_DIAL = 99
MIN_DIAL = 0

dialPosition = 50
number_of_zeros = 0

file_path = os.path.join(os.path.dirname(__file__), 'part1_input.txt')

def dial(direction, amount):
    global dialPosition
    global number_of_zeros
    reaminder = True
    amount = int(amount)

    while reaminder:
        if direction == 'L':
            if amount > dialPosition:
                amount -= dialPosition + 1
                dialPosition = MAX_DIAL
            else:
                dialPosition -= amount
                reaminder = False
        else:
            if amount >= 100 - dialPosition:
                amount -= 100 - dialPosition
                dialPosition = MIN_DIAL
            else:
                dialPosition += amount
                reaminder = False
    if dialPosition == 0:
        number_of_zeros += 1

with open(file_path, 'r') as file:
    for line in file:
        direction = line[0]
        amount = line[1:len(line)]
        
        dial(direction, amount)
    print(number_of_zeros)
            

