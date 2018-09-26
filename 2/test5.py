c = 0
with open('list.txt', 'r') as f:
    # s = f.readline()
    # print (s)
    for line in f :
        if "0" in line  :
            print(line)
            c+=1

print (c)