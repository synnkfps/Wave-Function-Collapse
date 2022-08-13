import random

#              0    1    2    3    4    5    6    7    8    9    10   11
characters = ["━", "┃", "┏", "┗", "┛", "┓", "┣", "┫", "┳", "┻", "╋", "|"]
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
    return characters[random.randrange(0, len(characters))] + random.choice(compatible[characters[random.randrange(0, len(characters))]])

t = 0

canvas1 = []
canvas2 = []
canvas3 = []

def randomize():
    t = characters[random.randrange(0, len(characters))]
    tt = random.choice(compatible[t])
    return t + tt

final_canvas = ''

# generate the canvas
for i in range(20):
    final_canvas += randomize()
    

queue = []
count = 0
cv = ''
# ╋┣

for i in final_canvas:
    queue.append(i)
    count += 1
    
    if len(queue)>2:
        queue.pop()
        if queue[1] in compatible[queue[0]]:
            cv += queue[1] + random.choice(compatible[queue[1]])
        else:
            ''''''
            print(queue[1], ' is not compatible with any of ', compatible[queue[0]])
    
print(cv)
