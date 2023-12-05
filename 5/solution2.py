from datetime import datetime
import re

start = datetime.now()

f = [x.removesuffix("\n") for x in list(open("5/input.txt", "r"))]

i = 0 #we will traverse through input for all elements this way

seeds = []
seed_soil = []
soil_fert = []
fert_water = []
water_light = []
light_temp = []
temp_humid = []
humid_loc = []

def next(arr, source): #given a dictionary and source number, return proper destination
    d = [arr[x] for x in range(0, len(arr), 3)]
    s = [arr[x] for x in range(1, len(arr), 3)]
    i = [arr[x] for x in range(2, len(arr), 3)]


    for j in range(len(s)):
        if source >= s[j] and source <= s[j] + i[j]:
            return d[j] + (source - s[j])
        
    return source

#seeds
seedsinput = [int(x) for x in re.findall("\d+", f[0])]
for k in range(0, len(seedsinput), 2):
    seeds.append(seedsinput[k], seedsinput[k + 1]) #store start and range length

#seed-soil
while f[i] != "seed-to-soil map:":
    i += 1
i += 1

while f[i] != "":
    seed_soil += [int(x) for x in re.findall("\d+", f[i])]
    i += 1
i += 1

#soil-fert
while f[i] != "soil-to-fertilizer map:":
    i += 1
i += 1

while f[i] != "":
    soil_fert += [int(x) for x in re.findall("\d+", f[i])]
    i += 1
i += 1

#fert-water
while f[i] != "fertilizer-to-water map:":
    i += 1
i += 1

while f[i] != "":
    fert_water += [int(x) for x in re.findall("\d+", f[i])]
    i += 1
i += 1

#water-light
while f[i] != "water-to-light map:":
    i += 1
i += 1

while f[i] != "":
    water_light += [int(x) for x in re.findall("\d+", f[i])]
    i += 1
i += 1

#light-temp
while f[i] != "light-to-temperature map:":
    i += 1
i += 1

while f[i] != "":
    light_temp += [int(x) for x in re.findall("\d+", f[i])]
    i += 1
i += 1

#temp-humid
while f[i] != "temperature-to-humidity map:":
    i += 1
i += 1

while f[i] != "":
    temp_humid += [int(x) for x in re.findall("\d+", f[i])]
    i += 1
i += 1

#humid-loc
while f[i] != "humidity-to-location map:":
    i += 1
i += 1

while i < len(f):
    humid_loc += [int(x) for x in re.findall("\d+", f[i])]
    i += 1

locs = []

for seed in seeds:
    soil = next(seed_soil, seed)
    fert = next(soil_fert, soil)
    water = next(fert_water, fert)
    light = next(water_light, water)
    temp = next(light_temp, light)
    humid = next(temp_humid, temp)
    loc = next(humid_loc, humid)
    locs.append(loc)
    print(seed, soil, fert, water, light, temp, humid, loc)


print(min(seeds))
print(min(locs))
print(datetime.now() - start)
    