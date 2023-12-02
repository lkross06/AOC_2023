f = open("1/input.txt", "r").readlines()
rtn = 0

for line in f: #go through each line
    #convert word numbers to line
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for word in words:
        index = line.find(word)
        if index != -1:
            #add the first letter of the word, the number, and the last letter of the word
            line = line[0:index+1] + str(words.index(word) + 1) + line[index+len(word)-1:]

    #find first and last numbers in string
    start = 0
    end = len(line) - 1

    a = 0 #first number
    b = 0 #second number

    while not(str(line[start]).isnumeric()):
        start += 1

    a = str(line[start])
    
    while not(str(line[end]).isnumeric()):
        end -= 1

    b = str(line[end])
    
    rtn += int(a + b)    

print(rtn)