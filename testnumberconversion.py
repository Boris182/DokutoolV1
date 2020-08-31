ext1from = "0416661000"
ext1to = "0416661499"

provider = "sbcon"

userconvdata = {}


with open("C:/Source20200821/number_conversion_print") as file:
    print("Load Extension File")
    nucondata = file.readlines()
    convdata = []
    print(nucondata[1])
    toentrypos = nucondata[1].find("Cnvtyp")
    tocnvtyppos = nucondata[1].find("Numtyp")
    tonumtyppos = nucondata[1].find("Rou")
    #toroupos = nucondata[1].find("Tardest")
    totardestpos = nucondata[1].find("Pre")
    toprepos = nucondata[1].find("Trc")
    totrcpos = nucondata[1].find("Newtyp")
    #tonewtyppos = nucondata[1].find("Cont")
    #tocontpos = nucondata[1].find("Bcap")
    #tobcappos = nucondata[1].find("Hlc")




for i in range(len(nucondata)):
    if nucondata[i][0].isdigit():
        # Numberentry Data
        numberentry = nucondata[i][:toentrypos].strip()
        # Conversiontype Data
        convtype = nucondata[i][toentrypos:tocnvtyppos].strip()
        # Numbertype Data
        numtype = nucondata[i][tocnvtyppos:tonumtyppos].strip()
        # Route Data
        #print(nucondata[i][tonumtyppos:toroupos])
        # Tardest Data
        #print(nucondata[i][toroupos:totardestpos])
        # Pre Data
        pre = nucondata[i][totardestpos:toprepos].strip()
        # Truncate Data
        truncate = nucondata[i][toprepos:totrcpos].strip()
        # Newtype Data
        #print(nucondata[i][totrcpos:tonewtyppos])
        # COnt Data
        #print(nucondata[i][tonewtyppos:tocontpos])
        # BCAP Data
        #print(nucondata[i][tocontpos:tobcappos])
        # Hlc Data
        #print(nucondata[i][tobcappos:])
        #print(numberentry)
        convdata.append([numberentry, convtype, numtype, pre, truncate])

# Check was für ein Provider es ist
if provider == "sbcon":
    ext1from = int(ext1from.replace("0", "41", 1))
    ext1to = int(ext1to.replace("0", "41", 1))
elif provider == "combridge":
    ext1from = int(ext1from)
    ext1to = int(ext1to)

# Estern nach Interne Nummern Check
for e in range(ext1from,ext1to + 1):
    if provider == "sbcon":
        e = str(e)
    elif provider == "combridge":
        e = "0" + str(e)
    for c in range(len(convdata)):
        if e[:len(convdata[c][0])] == convdata[c][0]:
            print("Extern - Intern")
            #print(convdata[c][0] + " " + convdata[c][4] + " " + convdata[c][3])
            intnumber = convdata[c][0][int(convdata[c][4]):] + convdata[c][3]
            extnumber = convdata[c][0].replace("41", "0", 1)
            clip = ""
            userconvdata[intnumber] = [intnumber, extnumber, clip]


# Intern nach Extern

print(userconvdata)











