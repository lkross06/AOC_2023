f = open("2/input.txt", "r").readlines()
rtn = 0 #12r, 13g, 14b

#find the number of cubes in a given set of a given color. return 0 if no data
def get_cubes(set, color):
    i = str(set).find(color)
    if i != -1:
        n = 1
        while str(set[i - n - 1:i]).isnumeric():
            n += 1
        
        return int(set[i - n: i])
    
    return 0

for l in f:
    line = l.removesuffix("\n")

    print(line)

    n = 1 #checks to see if theres more than one digit in the id number (i.e. > 10)
    while str(line[5:5+n+1]).isnumeric():
        n += 1
    id = int(line[5:5+n])
    valid = True

    line = line[6:]

    line = line.replace(" ", "")
    line = line.replace(",", "")

    sets = line.split(";")

    rmax = 0
    gmax = 0
    bmax = 0

    for i in sets:

        r = get_cubes(i, "red")
        b = get_cubes(i, "blue")
        g = get_cubes(i, "green")

        if r > rmax:
            rmax = r
        if g > gmax:
            gmax = g
        if b > bmax:
            bmax = b

    power = rmax * gmax * bmax

    print(rmax, gmax, bmax, power)
    
    rtn += power

print(rtn)




    

