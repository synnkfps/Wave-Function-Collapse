import random
import time

symbols = {
    "━": {"up": "000", "right": "010", "down": "000", "left": "010"},
    "┣": {"up": "010", "right": "010", "down": "010", "left": "000"},
    "┫": {"up": "010", "right": "000", "down": "010", "left": "010"},
    "┛": {"up": "000", "right": "010", "down": "010", "left": "010"},
    "┻": {"up": "010", "right": "010", "down": "000", "left": "010"},
    "┃": {"up": "010", "right": "000", "down": "010", "left": "000"},
    "╋": {"up": "010", "right": "010", "down": "010", "left": "010"},
    "┏": {"up": "000", "right": "010", "down": "010", "left": "000"},
    "┗": {"up": "010", "right": "010", "down": "000", "left": "000"},
    "┛": {"up": "010", "right": "000", "down": "000", "left": "010"},
    "┓": {"up": "000", "right": "000", "down": "010", "left": "010"},
}

empty = '░'
filled = '█'

# Render Function: renders a 3x3 representation using 4x3 metrics
def render(up, right, down, left) -> str:
    block = {'top': '000', 'middle': '010', 'bottom': '000'}  # layer composition

  # converting a 4 direction metrics into a 3x3 visualization needs to use the AND (&&) operator
  # so it will add 1 if one of the parts that is being checked has 1

  # top part
    block_list = list(block["top"])
    block_list = f'{empty if up[0] == "0" and left[0] == "0" else filled}{empty if up[1] == "0" else filled}{empty if up[2] == "0" and right[0] == "0" else filled}'
    block["top"] = block_list
  # middle part
    block_list = list(block["middle"])
    block_list = f'{empty if left[1] == "0" else filled}{filled}{empty if right[1] == "0" else filled}'
    block["middle"] = block_list
  # bottom part
    block_list = list(block["bottom"])
    block_list = f'{empty if down[2] == "0" and left[2] == "0" else filled}{empty if down[1] == "0" else filled}{empty if down[2] == "0" and right[2] == "0" else filled}'
    block["bottom"] = block_list

    bruh = []
    for i in list(block.values()):
        bruh.append(i)

    return bruh

symbol = '┏'

def char_metrics(char):
    tmp = [symbols[char]['up'],symbols[char]['right'],symbols[char]['down'],symbols[char]['left']]
    return tmp

def render_metrics(char):
    tmp = char_metrics(char)
    tmp = render(tmp[0], tmp[1], tmp[2], tmp[3])
    return tmp


# Connection Function: checks if a link between two characters exists
def connection(char1:str, char2:str, direction:str) -> bool:

    score = 0

    if direction == 'right':
        if render_metrics(char1)[0][2] == render_metrics(char2)[0][0]:
            score += 1
        print(render_metrics(char1)[0][2], render_metrics(char2)[0][0])
        if render_metrics(char1)[1][2] == render_metrics(char2)[1][0]:
            score += 1
        print(render_metrics(char1)[1][2], render_metrics(char2)[1][0])
        if render_metrics(char1)[2][2] == render_metrics(char2)[2][0]:
            score += 1
        print(render_metrics(char1)[2][2], render_metrics(char2)[2][0])
            

    return score

print(connection('┗','┛', 'right'))
