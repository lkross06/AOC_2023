f = list(open("4/input.txt", "r"))

rtn = 0
l = 0

def num_winners(line):
    line = line.split("|")[1:]

    win = [x for x in line[0].split(" ")]

    for i in win:
        if i == "":
            win.remove(i)

    given = [x for x in line[1].split(" ")]

    total = 0

    for i in given:
        if i in win:
            total += 1

    return total

while l < len(f):
    print(l, len(f))
    line = f[l].removesuffix("\n").replace(": ", "|")

    p = line.index("|")

    n = 0
    while str(line[p - n - 1:p]).isnumeric():
        n += 1
    
    number = int(line[p - n:p])

    total = num_winners(line)

    for i in range(1, total + 1):
        f.append(f[number - 1 + i])

    l += 1

print(len(f)) #wait for left number (current index) to catch up to right number (number of games so far)