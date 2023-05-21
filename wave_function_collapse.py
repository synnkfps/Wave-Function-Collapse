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

def render(up, right, down, left) -> str:
    empty = '░'
    filled = '█'

    lines = {'up': up, 'right': right, 'down': down, 'left': left}

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

    for i in list(block.values()):
        print(i)

symbol = '┃'
for i in symbols:
  render(symbols[i]['up'],symbols[i]['right'],symbols[i]['down'],symbols[i]['left'])
  print()
