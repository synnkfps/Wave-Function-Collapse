import random

#     0    1    2    3    4    5    6    7    8    9    10   11
c = ["━", "┃", "┏", "┗", "┛", "┓", "┣", "┫", "┳", "┻", "╋", " "]

# receive from left/right
bounding = {
    c[0]: [c[0], c[4], c[5], c[7], c[8], c[9], c[10]],
    c[1]: [c[2], c[3], c[6]],
    c[2]: [c[0], c[4], c[5], c[7], c[8], c[9], c[10]],
    c[3]: [c[0], c[4], c[5], c[7], c[8], c[9], c[10]],
    c[4]: [c[2], c[6]],
    c[5]: [c[2], c[6]],
    c[6]: [c[0], c[4], c[5], c[8], c[9], c[10]],
    c[7]: [c[1], c[2], c[3], c[6]],
    c[8]: [c[0], c[4], c[5], c[7], c[8], c[9], c[10]],
    c[9]: [c[0], c[4], c[5], c[7], c[8], c[9], c[10]],
    c[10]: [c[0], c[4], c[5], c[7], c[8], c[9], c[10]],
    c[11]: [c[1], c[2], c[3], c[6]]
}

output = ''
count = 0

# print(rand, bounding[rand])
for i in range(20):
    output += random.choice(c)

def rand_predict(t1, t2):
    return random.choice(t1[t2])

for j in output:
    index = output.index(j)
    current = output[index]
    before = output[index-1] if index > 0 else ''
    
    if before != '' and current in bounding[before]:
        pass
    elif before != '' and current not in bounding[before]:
        random_predict = rand_predict(bounding,before)

        print(f'Changing: "{output[index]}[{index}]" with "{random_predict}" because it isnt compatible with {before}')
        output = list(output)
        output[index] = random_predict
        output = ''.join(output)

    print(f'\tBefore: {before}\n\tCurrent: {output[index]}')

print(output)



# easier way to get a char before another

# string = 'abcdef'
# print(string[string.index('c')-1])

