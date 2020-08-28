import re

with open("C:/Source20200820/number_conversion_print") as file:
    print("Load Extension File")
    nucondata = file.readlines()
    print(nucondata[1])
    entry = nucondata[1].split("C")
    print(entry)
    print(len(entry[0]))
    print(nucondata[4][:len(entry[0])])




"""
externalnumbers = []
for p in range(41416661000, 41416661499 + 1):
    # externalnumbers.append("0" + str(p))
    externalnumbers.append(str(p))

#print(externalnumbers)

for i in range(len(nucondata)):
    if nucondata[i][0].isdigit():
        conversiondata = nucondata[i].split()
        #print(conversiondata)

        numberentry = conversiondata[0]
        truncate = int(conversiondata[4])
        pre = conversiondata[3]
        contype = conversiondata[1]
        numtype = conversiondata[2]
        convlist = [numberentry, truncate, pre]
        #print(convlist)

        #print(convlist)

        for e in externalnumbers:
            #print(e[:len(numberentry)])
            #print(len(numberentry))
            #print(type(numberentry))
            # print("0" + str(i))
            #num = str(e)
            if e[:len(numberentry)] == numberentry:

                #print("Yes es Matcht")
                print("Durchwahl: 0" + e[2:] + " Hat interne Nummer; " + str(pre) + e[truncate:])
                """


