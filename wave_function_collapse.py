import random

symbols = {
    "━": {"up": "000", "right": "010", "down": "000", "left": "010"},
    "┣": {"up": "010", "right": "010", "down": "010", "left": "000"},
    "┫": {"up": "010", "right": "000", "down": "010", "left": "010"},
    "┛": {"up": "010", "right": "000", "down": "000", "left": "010"},
    "┻": {"up": "010", "right": "010", "down": "000", "left": "010"},
    "┃": {"up": "010", "right": "000", "down": "010", "left": "000"},
    "╋": {"up": "010", "right": "010", "down": "010", "left": "010"},
    "┏": {"up": "000", "right": "010", "down": "010", "left": "000"},
    "┗": {"up": "010", "right": "010", "down": "000", "left": "000"},
    "┓": {"up": "000", "right": "000", "down": "010", "left": "010"},
}

size = 5

# Smarter dynamic implementation: each piece is automatically checked before it gets placed
output = ''
for i in range(size):
    if i == 0:
        rand_char = random.choice(list(symbols.keys()))
    else:
        x = random.choice(list(symbols.keys()))
        while not symbols[output[i-1]]['right'] == symbols[x]['left']:
            x = random.choice(list(symbols.keys()))
        else:
            rand_char=x
    output += rand_char
    
print(output)
