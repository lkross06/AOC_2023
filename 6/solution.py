from datetime import datetime
import re

start = datetime.now()

f = [x.removesuffix("\n") for x in list(open("6/input.txt", "r"))]

t = int("".join(re.findall("\d+", f[0])))
d = int("".join(re.findall("\d+", f[1])))

def get_num_winners(total_time, threshold_distance): #i think the d(t) function is concave + quadratic
    i = 1
    j = total_time

    d1 = 0
    d2 = 0

    while i <= j and d1 <= threshold_distance and d2 <= threshold_distance:
        d1 = (total_time - i) * i
        d2 = (total_time - j) * j

        if d1 <= threshold_distance:
            i += 1

        if d2 <= threshold_distance:
            j -= 1

    return j - i + 1

print(t, d)
product = get_num_winners(t, d)

print(product)
print(datetime.now()-start)

    