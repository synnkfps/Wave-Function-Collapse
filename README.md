# Wave Function Collapse
## pythonic way of doing it

`Started: 13/08/2022`<br>
`Ended: N/A`

### the theory
get an list of characters that has connections between them: 
```
━ ┣ ┫ ┳ ┻ 
```
put all of them randomly placed into a "canvas", then organizing them into ways that they makes "sense" (intelligently placed), a way that they connects between themselves without getting messy.

### initial code theory
my code theory does not uses an advanced algorithm, only logic...

- put the first character randomly
- the next character will check the last one
- then it will check if the predicted character is in one of the compatible neighbours of the last character
- if it is, place it
- - else: put a random character that IS a compatible neighbour
- do the same with the rest

### how output should look like
```txt
┏━┫┣╋┳┓
┣━╋┻┻┫┃
┣━╋┳━┻┫
┗━┻┻━━┛
```
