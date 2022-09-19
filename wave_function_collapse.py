import random

#     0   1    2    3    4    5    6    7    8    9    10   11
c = ["━","┣", "┫", "┳", "┻", "", "┃", "╋", "┏", "┗", "┛", "┓"]
# receive from left/right
side_bounding = {
    c[0]: {
        "left": [c[0], c[1], c[3], c[4], c[7], c[8], c[9]], 
        "right": [c[0], c[2], c[3], c[4], c[7], c[10], c[11]]
    },
    c[1]: {
        "left": [c[2], c[5], c[6]],
        "right": [c[0], c[2], c[3], c[4], c[7], c[10], c[11]]
    },
    c[2]: {
        "left": [c[0], c[1], c[3], c[4], c[7], c[8], c[9]],
        "right": [c[1], c[5], c[6]]
    },
    c[3]: {
        "left": [c[0], c[1], c[3], c[4], c[7], c[8], c[9]],
        "right": [c[0], c[2], c[3], c[4], c[7], c[10], c[11]]
    },
    c[4]: {
        "left": [c[0], c[1], c[3], c[4], c[7], c[8], c[9]],
        "right": [c[0], c[2], c[3], c[4], c[7], c[10], c[11]]
    },
    c[5]: {
        "left": [c[2], c[5]],
        "right": [c[1], c[5]]
    },
    c[6]: {
        "left": [c[2], c[6]],
        "right": [c[1], c[6]]
    }, 
    c[7]: {
        "left": [c[0], c[1], c[3], c[4], c[7], c[8], c[9]],
        "right": [c[0], c[2], c[3], c[4], c[7], c[10], c[11]]
    },
    c[8]: {
        "left": [c[2], c[5], c[6], c[10], c[11]],
        "right": [c[0], c[2], c[3], c[4], c[7], c[10], c[11]]
    },
    c[9]: {
        "left": [c[2], c[5], c[6], c[10], c[11]],
        "right": [c[0], c[2], c[3], c[4], c[7], c[10], c[11]]
    },
    c[10]: {
        "left": [c[0], c[1], c[3], c[4], c[7], c[8], c[9]],
        "right": [c[1], c[5], c[6], c[8], c[9]],
    },
    c[11]: {
        "left": [c[0], c[1], c[3], c[4], c[7], c[8], c[9]],
        "right": [c[1], c[5], c[6], c[8], c[9]]
    }
}
#     0   1    2    3    4    5    6    7    8    9    10   11
c = ["━","┣", "┫", "┳", "┻", "", "┃", "╋", "┏", "┗", "┛", "┓"]
output = []
size = 30

for i in range(size):
    rand1 = random.choice(c)
    rand2 = random.choice(c)
    if rand1 in side_bounding[rand2][random.choice(['left'])]:
        output.append(rand1)
        output.append(rand2)
    else:
        rand1 = random.choice(c)
        rand2 = random.choice(c)
    if rand1 in side_bounding[rand2][random.choice(['right'])]:
        output.append(rand2)
        output.append(rand1)
    else:
        rand2 = random.choice(c)
        rand1 = random.choice(c)
else:
    for i in range(len(output)):
        for k, v in enumerate(output):
            try:
                if output[k] in side_bounding[output[k+1]]['left']:
                    #print(f'{output[k]} bounds with {output[k+1]} from left ({output[k]}{output[k+1]})')
                    pass
                else:
                    rLeft = random.choice(side_bounding[output[k+1]]['left'])
                    print(f'(left) ({k}) changing {output[k]} to {rLeft} so it can bound to {output[k+1]} ({rLeft}{output[k+1]})')
                    output[k] = rLeft
                if output[k] in side_bounding[output[k-1]]['right']:
                    #print(f'{output[k]} bounds with {output[k-1]} from right({output[k-1]}{output[k]})')
                    pass
                else:
                    rRight = random.choice(side_bounding[output[k-1]]['right'])
                    print(f'(right) ({k}) changing {output[k]} to {rRight} so it can bound to {output[k-1]} ({output[k-1]}{rRight})')
                    output[k] = rRight
            except:
                pass

print('\n'+''.join(output))
