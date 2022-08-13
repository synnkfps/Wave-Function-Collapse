import random

#              0    1    2    3     4    5    6    7    8    9    10  11
characters = ["━", "┃", "┏", "┗", "┛", "┓", "┣", "┫", "┳", "┻", "╋", " "]
c = characters

compatible = {
    characters[0]: [c[4], c[5], c[7], c[8], c[9], c[10]],
    characters[1]: [c[11], c[6]],
    characters[2]: [c[0], c[4], c[5], c[7], c[8], c[9], c[10]],
    characters[3]: [c[0], c[4], c[7], c[8], c[9], c[10]],
    characters[4]: [c[11]],
    characters[5]: [c[11]],
    characters[6]: [c[0], c[4], c[5], c[7], c[8], c[9], c[10]],
    characters[7]: [c[11]],
    characters[8]: [c[0], c[8], c[9], c[10]],
    characters[9]: [c[0], c[8], c[9], c[10]],
    characters[10]: [c[0], c[8], c[9], c[10]],
    characters[11]: [c[1], c[3], c[6]]
}


def gen_c():
    random_char = characters[random.randrange(0, len(characters))]
    random_compatible = random.choice(compatible[random_char])

    return random_char + random_compatible + '\n'

canvas = ''

t = 0

while t < 50:
    canvas += gen_c()
    t += 1

print(canvas)
