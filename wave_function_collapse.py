import random

symbols = {
    "┃": {"up": "010", "right": "000", "down": "010", "left": "000"},
    "━": {"up": "000", "right": "010", "down": "000", "left": "010"},
    "┣": {"up": "010", "right": "010", "down": "010", "left": "000"},
    "┫": {"up": "010", "right": "000", "down": "010", "left": "010"},
    "┳": {"up": "000", "right": "010", "down": "010", "left": "010"},
    "┻": {"up": "010", "right": "010", "down": "000", "left": "010"},
    "╋": {"up": "010", "right": "010", "down": "010", "left": "010"},
    "┏": {"up": "000", "right": "010", "down": "010", "left": "000"},
    "┗": {"up": "010", "right": "010", "down": "000", "left": "000"},
    "┓": {"up": "000", "right": "000", "down": "010", "left": "010"},
    "┛": {"up": "010", "right": "000", "down": "000", "left": "010"},
    " ": {"up": "000", "right": "000", "down": "000", "left": "000"},
    
}

size = 7
layer_amount = 3

output = ''
for i in range(size):
    if i == 0:
        rand_char = random.choice(list(symbols.keys()))
    else:
        x = random.choice(list(symbols.keys()))
        while not symbols[output[i-1]]['right'] == symbols[x]['left']:
            x = random.choice(list(symbols.keys()))
        else:
            rand_char = x
    output += rand_char

layers = [output]
actual_layer = 0
for j in range(layer_amount):
    tmp = ''
    for i in range(size):
        if i == 0:
            rand_char = random.choice(list(symbols.keys()))

            while not symbols[rand_char]['up'] == symbols[layers[actual_layer][i]]['down']:
                rand_char = random.choice(list(symbols.keys()))
        else:
            x = random.choice(list(symbols.keys()))
            while not symbols[x]['up'] == symbols[layers[actual_layer][i]]['down'] or not symbols[tmp[i-1]]['right'] == symbols[x]['left']:
                x = random.choice(list(symbols.keys()))

            rand_char = x
            
        tmp += rand_char
    layers.append(tmp)
    actual_layer += 1

print('\n'.join(layers))
print()

layers_copy = []
for i in layers:
    line = ''
    for j, x in enumerate(i):
        line += x
    
    line = ('┣' if symbols[line[0]]['left'] == '010' else '┃')+line+('┫'if symbols[line[-1]]['right'] == '010' else '┃')
    layers_copy.append(line)

line = list('┏'+'━'*size+'┓')
bruh = ''
for x,i in enumerate(line):
    if x > 0 and x <= size:
        if symbols[layers_copy[0][x]]['up'] == '010':
            i = '┳'
    bruh += i

print(bruh)
for i in layers_copy:
    print(i)

line = list('┗'+'━'*size+'┛')
bruh = ''
for x,i in enumerate(line):
    if x > 0 and x <= size:
        if symbols[layers_copy[-1][x]]['down'] == '010':
            i = '┻'
    bruh += i

print(bruh)
