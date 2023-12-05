from datetime import datetime
import re

start = datetime.now()

f = [x.removesuffix("\n") for x in list(open("5/input.txt", "r"))]

i = 0 #we will traverse through input for all elements this way

seeds = []
seed_soil = {}
soil_fert = {}
fert_water = {}
water_light = {}
light_temp = {}
temp_humid = {}
humid_loc = {}

#returns a dictionary given the destination start, source start, and range length
def get_dict(dest_start, source_start, length):
    d = {}

    for i in range(length):
        d[source_start + i] = dest_start + i
    
    return d

def next(dict, source): #given a dictionary and source number, return proper destination
    rtn = dict.get(source)
    if rtn == None:
        return source
    return rtn


#seeds
seeds = [int(x) for x in re.findall("\d+", f[0])]

#seed-soil
while f[i] != "seed-to-soil map:":
    i += 1
i += 1

while f[i] != "":
    nums1 = [int(x) for x in re.findall("\d+", f[i])]
    seed_soil.update(get_dict(nums1[0], nums1[1], nums1[2]))
    i += 1
i += 1

print("seed soil done")

#soil-fert
while f[i] != "soil-to-fertilizer map:":
    i += 1
i += 1

while f[i] != "":
    nums1 = [int(x) for x in re.findall("\d+", f[i])]
    soil_fert.update(get_dict(nums1[0], nums1[1], nums1[2]))
    i += 1
i += 1

print("soil fert done")

#fert-water
while f[i] != "fertilizer-to-water map:":
    i += 1
i += 1

while f[i] != "":
    nums1 = [int(x) for x in re.findall("\d+", f[i])]
    fert_water.update(get_dict(nums1[0], nums1[1], nums1[2]))
    i += 1
i += 1

print("fert water done")


#water-light
while f[i] != "water-to-light map:":
    i += 1
i += 1

while f[i] != "":
    nums1 = [int(x) for x in re.findall("\d+", f[i])]
    water_light.update(get_dict(nums1[0], nums1[1], nums1[2]))
    i += 1
i += 1

print("water light done")


#light-temp
while f[i] != "light-to-temperature map:":
    i += 1
i += 1

while f[i] != "":
    nums1 = [int(x) for x in re.findall("\d+", f[i])]
    light_temp.update(get_dict(nums1[0], nums1[1], nums1[2]))
    i += 1
i += 1

print("light temp done")


#temp-humid
while f[i] != "temperature-to-humidity map:":
    i += 1
i += 1

while f[i] != "":
    nums1 = [int(x) for x in re.findall("\d+", f[i])]
    temp_humid.update(get_dict(nums1[0], nums1[1], nums1[2]))
    i += 1
i += 1

print("temp humid done")


#humid-loc
while f[i] != "humidity-to-location map:":
    i += 1
i += 1

while i < len(f):
    nums1 = [int(x) for x in re.findall("\d+", f[i])]
    humid_loc.update(get_dict(nums1[0], nums1[1], nums1[2]))
    i += 1

print("humid loc done")


# print(seeds)
# print(seed_soil)
# print(soil_fert)
# print(fert_water)
# print(water_light)
# print(light_temp)
# print(temp_humid)
# print(humid_loc)

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


print(min(locs))
print(datetime.now() - start)
    