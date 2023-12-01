upCount = 0
downCount = 0

with open('input.txt') as f:
    content = f.read()

for c in content:
    if c == '(':
        upCount += 1
    else:
        downCount += 1

print(upCount - downCount)