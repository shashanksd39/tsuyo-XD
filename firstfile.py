#file handling stuff
f = open("firstfile.txt")
content = f.read()
print(content)
f.close()


f = open("firstfile.txt",'a')
f.write("this is the thing i wrote after.\n")
f.close()