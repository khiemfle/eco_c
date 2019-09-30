f = open("note11.txt", "r")
str = " "
arr = []
while str != "":
    str = f.readline()
    if str in arr :
        print(str)
    else:
        arr.append(str)