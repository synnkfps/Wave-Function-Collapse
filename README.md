# Wave-Function-Collapse
## pythonic way of doing it

`Started: 13/08/2022`<br>
`Ended: N/A`

### the theory
get an list of characters that has connections between them: 
```
━ ┃ ┏ ┗ ┛ ┓ ┣ ┫ ┳ ┻ ╋ 
```
put all of them randomly placed into a "canvas", then organizing them into ways that they makes "sense" (intelligently placed), a way that they connects between themselves without getting messy.

### initial code theory
my code theory does not uses an advanced algorithm, only logic...

- make all the characters a dict with its available neighbour char
- then select one of the available neighbour char randomly and place it
- on the rest of the canvas do the same thing, but preferrably have a "edged" end

### how output should look like
```txt
┏━┫┣╋┳┓
┣━╋┻┻┫┃
┣━╋┳━┻┫
┗━┻┻━━┛
```
