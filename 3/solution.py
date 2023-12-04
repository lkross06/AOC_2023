f = open("3/input.txt", "r").readlines()

cols = len(f[0]) - 1 #remove "\n"
rows = len(f)

#replace all "\n" with "." so there no numbers on the right edge
#doesn't really account for last line of code but it's not in my puzzle input :D
grid = [[x for x in str(l).replace("\n", ".")] for l in f] #2d arrayd
gear_adjs = {}

total = 0 #return value
product = 0 #part 2 return value

def get_adjacents(r, cs): #r = row where the number is, cs = array of cols that digits span across
    checkleft = cs[0] > 0
    checkright = cs[len(cs) - 1] < cols - 1
    checkup = r > 0
    checkdown = r < rows - 1

    rtn = [] #list of adjacents
    gears = [] #list of [r, c] for gears (*). if its not a gear, -1

    csstart = cs[0] #what column to start checking on
    csend = cs[len(cs) - 1] #what column to end on
    downstart = cs[0]
    downend = cs[len(cs) - 1]

    if checkleft:
        left = grid[r][cs[0] - 1]
        rtn.append(left)

        if left == "*":
            gears.append([r, cs[0] - 1])
        else:
            gears.append(-1)

        csstart -= 1
        downstart -= 1
        
    if checkright:
        right = grid[r][cs[len(cs) - 1] + 1]
        rtn.append(right)

        if right == "*":
            gears.append([r, cs[len(cs) - 1] + 1])
        else:
            gears.append(-1)

        csend += 1
        downend += 1

    if checkup:
        for c in range(csstart, csend + 1):
            up = grid[r - 1][c]
            rtn.append(up)

            if up == "*":
                gears.append([r - 1, c])
            else:
                gears.append(-1)

    if checkdown:
        for c in range(downstart, downend + 1):
            down = grid[r + 1][c]
            rtn.append(down)

            if down == "*":
                gears.append([r + 1, c])
            else:
                gears.append(-1)

    return [rtn, gears]

def rc_to_str(rc): #rc = pos in the form [r, c]
    return str(rc[0]) + ", " + str(rc[1])

for r in range(0, len(grid)):
    c = 0
    while c < len(grid[r]):
        curr = str(grid[r][c])
        n = 0
        if curr.isnumeric():
            while c < cols:
                if str(grid[r][c + n]).isnumeric():
                    n += 1
                else:
                    break
        
            cs = [c + x for x in range(n)]
            full_num = int("".join([grid[r][c] for c in cs]))
            adjs = get_adjacents(r, cs)
            gears = adjs[1]
            adjs = adjs[0]

            for x in range(len(adjs)):
                i = adjs[x]
                if i != ".":
                    total += full_num
                if i == "*":
                    key = rc_to_str(gears[x])
                    if not(key in gear_adjs.keys()):
                        gear_adjs[key] = [full_num]
                    else:
                        gear_adjs[key].append(full_num)

        c += n + 1

for key in gear_adjs.keys():
    arr = gear_adjs[key]
    if len(arr) == 2:
        product += (arr[0] * arr[1])

print(product)