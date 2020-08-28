numberentry = "041268161"
truncate = 7
externalnumbers = []
pre = "1"

for i in range(412681600,412681699 + 1):
    externalnumbers.append("0" + str(i))

print(externalnumbers)


for i in externalnumbers:
    #print("0" + str(i))
    num = str(i)
    if i[:len(numberentry)] == numberentry:
        print("Durchwahl: " + i + " Hat interne Nummer; " + str(pre) + i[truncate:])
