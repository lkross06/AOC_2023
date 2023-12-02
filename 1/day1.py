f = open("1/input.txt", "r").readlines()
rtn = 0

for l in f: #go through each line
    line = l.removesuffix("\n")
    print(line)
    #convert word numbers to line
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    first_occur = len(line) - 1
    first_word = ""
    last_occur = 0
    last_word = ""

    for word in words:
        i = line.find(word)
        if i < first_occur and i != -1:
            first_word = word
            first_occur = i

        j = line.rfind(word)
        if j > last_occur and i != -1:
            last_word = word
            last_occur = j
        
    print(first_word, first_occur, last_word, last_occur)

    line = [x for x in line]
    if last_word != "":
        line[last_occur] = str(words.index(last_word) + 1)
    if first_word != "":
        line[first_occur] = str(words.index(first_word) + 1)

    line = "".join(line)

    print(line)

    #find first and last numbers in string
    start = 0
    end = len(line) - 1

    digits = [] #first and last number

    while not(str(line[start]).isnumeric()):
        start += 1

    digits += str(line[start])
    
    while not(str(line[end]).isnumeric()):
        end -= 1

    digits += str(line[end])
    
    rtn += int("".join(digits))

print(rtn)