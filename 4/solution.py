f = open("4/input.txt", "r")

rtn = 0

for l in range(len(f)):
    line = f[l].removesuffix("\n").replace(": ", "|")

    line = line.split("|")[1:]

    print(line)

    win = [x for x in line[0].split(" ")]

    for i in win:
        if i == "":
            win.remove(i)

    given = [x for x in line[1].split(" ")]

    for i in given:
        if i == "":
            given.remove(i)

    total = 0

    for i in given:
        if i in win:
            if total == 0:
                total = 1
            else:
                total *= 2
    
    print(total)

    rtn += total

print(rtn)