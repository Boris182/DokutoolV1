import importdata
import exportdata

customerdata = {"Kundenname": "00325-Parcom", "Adresse": "Hasliring 1", "Ort": "6032 Emmen"}

siriodata = importdata.Importsiriodata()


sirioexport = exportdata.Exportsirio("./files/",
                                     customerdata,
                                     siriodata.querydata,
                                     siriodata.dataCont,
                                     siriodata.dataEspa,
                                     siriodata.dataJob)

sirioexport.writesiriodata()



#mxonedata = importdata.Importuserdata("C:/Source20200821")

#mxonedata.importuserdata()
#mxonedata.createuserdata()
#mxonedata.print_users()
#print(mxonedata.users)
#print(customerdata)

#mxoneexport = testexcel.Exportmxone("C:/", customerdata, mxonedata.users, "Systemdata")
#mxoneexport.printmxonedata()
#mxoneexport.writemxonedata()














"""
mxonesystemdata = {}

with open("C:/Source20200820/ts_about") as file:
    print("Load Extension File")
    ts_aboutdata = file.readlines()
    print(ts_aboutdata)
    file.close()


for i in ts_aboutdata:
    if "Version: " in i:
        mxonesystemdata["mxversion"] = i.partition("Version: ")[2].replace("\n", "", 1)
    elif " MX-ONE Service Node Manager " in i:
        mxonesystemdata["snmversion"] = i.partition(" MX-ONE Service Node Manager ")[2].replace(" :\n", "", 1)
    elif " MX-ONE Provisioning Manager " in i:
        mxonesystemdata["pmversion"] = i.partition(" MX-ONE Provisioning Manager ")[2].replace(" :\n", "", 1)

print(mxonesystemdata)

with open("C:/Source20200820/mxone_data") as file:
    print("Load Extension File")
    mxone_datadata = file.readlines()
    print(mxone_datadata)
    file.close()

for i in mxone_datadata:
    if "lim" in i:
        i = i.split()
        # 1 ist Hostname, 2 ist IP, 3 ist lim x
        mxonesystemdata[i[3]] = [i[1], i[2]]
    elif "c-" in i:
        i = i.split()
        # 0 ist Server Name, 1 ist IP des Lims, 3 ist IP der DB
        mxonesystemdata["Cassandra " + i[0]] = [i[1], i[3]]


with open("C:/Source20200820/media_gateway_info_general") as file:
    print("Load Extension File")
    mgudata = file.readlines()
    print(mgudata)
    file.close()

    gwnumber = 0
    for l in mgudata:
        if " SW information" in l:
            l = l.split()
            gwnumber = gwnumber + 1
            mxonesystemdata["gateway"+ str(gwnumber)] = [l[1]]
        elif "MGW version: " in l:
            l = l.split()
            mxonesystemdata["gateway"+ str(gwnumber)].append(l[2])
        elif "Media gateway type: " in l:
            l = l.split()
            mxonesystemdata["gateway"+ str(gwnumber)].append(l[3] + " " + l[4])
        elif "Board revision: " in l:
            l = l.split()
            mxonesystemdata["gateway"+ str(gwnumber)].append(l[2])
        elif "Board serial number: " in l:
            l = l.split()
            mxonesystemdata["gateway"+ str(gwnumber)].append(l[3])


for i in mxonesystemdata:
    print(i + " " + str(mxonesystemdata[i]))
"""