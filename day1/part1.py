with open('input.txt') as file:
    lines = file.readlines()

ans = 0
for line in lines:
    first = 0
    last = 0
    for c in line:
        if c.isdigit() and not first:
            first = c
        elif c.isdigit():
            last = c
    
    if last == 0:
        ans += int(first + first)
    else:
        ans += int(first + last)

print(ans)
    