f = open("3/input.txt", "r").readlines()

cols = len(f[0]) - 1 #remove "\n"
rows = len(f)

#replace all "\n" with "." so there no numbers on the right edge
#doesn't really account for last line of code but it's not in my puzzle input :D
grid = [[x for x in str(l).replace("\n", ".")] for l in f] #2d arrayd

total = 0 #return value

def get_adjacents(r, cs): #r = row where the number is, cs = array of cols that digits span across
    checkleft = cs[0] > 0
    checkright = cs[len(cs) - 1] < cols - 1
    checkup = r > 0
    checkdown = r < rows - 1

    rtn = []

    csstart = cs[0] #what column to start checking on
    csend = cs[len(cs) - 1] #what column to end on
    downstart = cs[0]
    downend = cs[len(cs) - 1]

    if checkleft:
        rtn.append(grid[r][cs[0] - 1])
        csstart -= 1
        downstart -= 1
        
    if checkright:
        rtn.append(grid[r][cs[len(cs) - 1] + 1])
        csend += 1
        downend += 1

    if checkup:
        for c in range(csstart, csend + 1):
            rtn.append(grid[r - 1][c])

    if checkdown:
        for c in range(downstart, downend + 1):
            rtn.append(grid[r + 1][c])

    return rtn

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

            for i in adjs:
                if i != ".":
                    total += full_num

        c += n + 1

print(total)