import fdb


class Importuserdata():

    def __init__(self, path, customerdata):
        self.users = {}
        self.path = path
        self.extensiondata = []
        self.name1data = []
        self.dect_extensiondata = []
        self.ip_extensiondata = []
        self.exddpdata = []
        self.ksddpdata = []
        self.parallel_ringingdata = []
        self.nucondata = []
        self.convdata = []
        self.users = {}
        self.customerdata = customerdata
        self.extnumberrange = []
        self.clipdata = []

    def print_users(self):
        for i in self.users:
            print(self.users[i])

    def importuserdata(self):

        with open(self.path + "/extension") as file:
            print("Load Extension File")
            self.extensiondata = file.readlines()
            print(self.extensiondata[0])
            file.close()

        with open(self.path + "/name1", encoding='utf-8') as file:
            print("Load Extension File")
            self.name1data = file.readlines()
            print(self.name1data[0])
            file.close()

        with open(self.path + "/dect_extension") as file:
            print("Load Extension File")
            self.dect_extensiondata = file.readlines()
            print(self.dect_extensiondata[0])
            file.close()

        with open(self.path + "/ip_extension") as file:
            print("Load Extension File")
            self.ip_extensiondata = file.readlines()
            print(self.ip_extensiondata[0])
            file.close()

        with open(self.path + "/EXDDP") as file:
            print("Load Extension File")
            self.exddpdata = file.readlines()
            print(self.exddpdata[0])
            file.close()

        with open(self.path + "/KSDDP") as file:
            print("Load Extension File")
            self.ksddpdata = file.readlines()
            print(self.ksddpdata[0])
            file.close()

        with open(self.path + "/parallel_ringing") as file:
            print("Load Extension File")
            self.parallel_ringingdata = file.readlines()
            print(self.parallel_ringingdata[0])
            file.close()

        with open(self.path + "/number_conversion_print") as file:
            self.nucondata = file.readlines()
            toentrypos = self.nucondata[1].find("Cnvtyp")
            tocnvtyppos = self.nucondata[1].find("Numtyp")
            tonumtyppos = self.nucondata[1].find("Rou")
            totardestpos = self.nucondata[1].find("Pre")
            toprepos = self.nucondata[1].find("Trc")
            totrcpos = self.nucondata[1].find("Newtyp")

            for i in range(len(self.nucondata)):
                if self.nucondata[i][0].isdigit():
                    # Numberentry Data
                    numberentry = self.nucondata[i][:toentrypos].strip()
                    # Conversiontype Data
                    convtype = self.nucondata[i][toentrypos:tocnvtyppos].strip()
                    # Numbertype Data
                    numtype = self.nucondata[i][tocnvtyppos:tonumtyppos].strip()
                    # Reserve Route Data
                    # Reserve print(nucondata[i][tonumtyppos:toroupos])
                    # Reserve Tardest Data
                    # Reserve print(nucondata[i][toroupos:totardestpos])
                    # Pre Data
                    pre = self.nucondata[i][totardestpos:toprepos].strip()
                    # Truncate Data
                    truncate = self.nucondata[i][toprepos:totrcpos].strip()
                    if truncate == "":
                        truncate = "0"
                    # Reserve Newtype Data
                    # Reserve print(nucondata[i][totrcpos:tonewtyppos])
                    # Reserve Cont Data
                    # Reserve print(nucondata[i][tonewtyppos:tocontpos])
                    # Reserve BCAP Data
                    # Reserve print(nucondata[i][tocontpos:tobcappos])
                    # Reserve Hlc Data
                    # Reserve print(nucondata[i][tobcappos:])
                    # Reserve print(numberentry)
                    self.convdata.append([numberentry, convtype, numtype, pre, truncate])

            print(self.nucondata[0])
            file.close()

    # Erstellt und Sortiert das User Dictionary, fügt alle Dateien zusammen und ergänzt diese
    def createuserdata(self):
        # Prüfen was für ein Provider, für die Externe Nummerzuweisung

        # SBCON?
        if self.customerdata["Provider"] == "sbcon":
            try:
                self.ext1from = int(self.customerdata["Nummerbereichfrom1"].replace("0", "41", 1))
                self.ext1to = int(self.customerdata["Nummerbereichto1"].replace("0", "41", 1))
            except ValueError:
                "Nummerbereich 1 nicht angegeben"
            try:
                self.ext2from = int(self.customerdata["Nummerbereichfrom2"].replace("0", "41", 1))
                self.ext2to = int(self.customerdata["Nummerbereichto2"].replace("0", "41", 1))
            except ValueError:
                "Nummerbereich 2 nicht angegeben"
            try:
                self.ext3from = int(self.customerdata["Nummerbereichfrom3"].replace("0", "41", 1))
                self.ext3to = int(self.customerdata["Nummerbereichto3"].replace("0", "41", 1))
            except ValueError:
                "Nummerbereich 3 nicht angegeben"

        # Combridge?
        elif self.customerdata["Provider"] == "combridge":
            try:
                self.ext1from = int(self.customerdata["Nummerbereichfrom1"])
                self.ext1to = int(self.customerdata["Nummerbereichto1"])
            except ValueError:
                "Nummerbereich 1 nicht angegeben"

            try:
                self.ext2from = int(self.customerdata["Nummerbereichfrom2"])
                self.ext2to = int(self.customerdata["Nummerbereichto2"])
            except ValueError:
                "Nummerbereich 2 nicht angegeben"

            try:
                self.ext3from = int(self.customerdata["Nummerbereichfrom3"])
                self.ext3to = int(self.customerdata["Nummerbereichto3"])
            except ValueError:
                "Nummerbereich 3 nicht angegeben"

        # Kein Provider ausgewählt, es wird einfach ein Integer gemacht
        else:
            self.ext1from = int(self.customerdata["Nummerbereichfrom1"])
            self.ext1to = int(self.customerdata["Nummerbereichto1"])
            self.ext2from = int(self.customerdata["Nummerbereichfrom2"])
            self.ext2to = int(self.customerdata["Nummerbereichto2"])
            self.ext3from = int(self.customerdata["Nummerbereichfrom3"])
            self.ext3to = int(self.customerdata["Nummerbereichto3"])

        # Erstellen und Befüllen des User Dictionary

        # Verarbeitet die Extension Daten in das User Dictionary
        for i in range(len(self.extensiondata)):
            if self.extensiondata[i][0].isdigit():
                userdata = self.extensiondata[i].split()

                number = str(userdata[0])
                server = str(userdata[2])
                csp = str(userdata[3])
                virtual = userdata[4]
                third = userdata[13]
                list = [number, virtual, "", "", "", csp, server, "", "", third, "", ""]

                if number in self.users:
                    self.users[number] = list
                else:
                    self.users[number] = list

        # Verarbeitet die name1 Daten in das User Dictionary
        for i in range(len(self.name1data)):
            if self.name1data[i][0].isdigit():
                userdata = self.name1data[i].split()

                number = str(userdata[0])
                name1 = userdata[4].strip('\"')
                name2 = userdata[5].strip('\"')
                list = [number, "", "", name1, name2, "", "", "", "", "", "", ""]

                if number in self.users:
                    self.users[number][0] = number
                    self.users[number][3] = name1
                    self.users[number][4] = name2
                else:
                    self.users[number] = list

        # Verarbeitet die dect_extension Daten in das User Dictionary
        for i in range(len(self.dect_extensiondata)):
            if self.dect_extensiondata[i][0].isdigit():
                userdata = self.dect_extensiondata[i].split()

                number = str(userdata[0])
                list = [number, "DECT", "", "", "", "", "", "", "", "", "", ""]

                if number in self.users:
                    self.users[number][0] = number
                    self.users[number][1] = "DECT"
                else:
                    self.users[number] = list

        # Verarbeitet die ip_extension Daten in das User Dictionary
        for i in range(len(self.ip_extensiondata)):
            if self.ip_extensiondata[i][0].isdigit():
                userdata = self.ip_extensiondata[i].split()

                number = str(userdata[0])
                iptype = userdata[1]
                list = [number, iptype, "", "", "", "", "", "", "", "", "", ""]

                if number in self.users:
                    self.users[number][0] = number
                    self.users[number][1] = iptype
                else:
                    self.users[number] = list

        # Verarbeitet die EXDDP Daten in das User Dictionary
        for i in range(len(self.exddpdata)):
            if self.exddpdata[i][0].isdigit():
                userdata = self.exddpdata[i].split()

                number = str(userdata[0])
                address = userdata[1]
                cat = str(userdata[2])
                list = [number, "Analog", address, "", "", cat, "", "", "", "", "", ""]

                if number in self.users:
                    self.users[number][0] = number
                    self.users[number][1] = "Analog"
                    self.users[number][2] = address
                    self.users[number][5] = cat
                else:
                    self.users[number] = list

        # Verarbeitet die KSDDP Daten in das User Dictionary
        for i in range(len(self.ksddpdata)):
            if self.ksddpdata[i][0].isdigit():
                userdata = self.ksddpdata[i].split()

                number = str(userdata[0])
                address = userdata[1]
                cat = str(userdata[2])
                list = [number, "Digital", address, "", "", cat, "", "", "", "", "", ""]

                if number in self.users:
                    self.users[number][0] = number
                    self.users[number][1] = "Digital"
                    self.users[number][2] = address
                    self.users[number][5] = cat
                else:
                    self.users[number] = list

        # Verarbeitet die  Parallel Ringing Daten in das User Dictionary
        for i in range(len(self.parallel_ringingdata)):
            if self.parallel_ringingdata[i][0].isdigit():
                userdata = self.parallel_ringingdata[i].split()

                number = str(userdata[0])
                secondary1 = ""
                secondary2 = ""
                list = []
                if len(userdata) == 4:
                    secondary1 = str(userdata[1])
                    secondary2 = str(userdata[2])
                    list = [number, "", "", "", "", "", "", secondary1, secondary2, "", "", ""]
                elif len(userdata) == 3:
                    secondary1 = str(userdata[1])
                    secondary2 = ""
                    list = [number, "", "", "", "", "", "", secondary1, "", "", "", ""]

                if number in self.users:
                    self.users[number][0] = number
                    self.users[number][7] = secondary1
                    self.users[number][8] = secondary2
                else:
                    self.users[number] = list

        # Verarbeitet die Number Conversion Daten im das User Dictionary
        # Verbindet alle Externen Nummerbereiche in eine Liste, mehrere Ranges sogesagt

        try:
            self.extnumberrange.extend(range(self.ext1from, self.ext1to + 1))
        except AttributeError:
            print("Keine Daten")

        try:
            self.extnumberrange.extend(range(self.ext2from, self.ext2to + 1))
        except AttributeError:
            print("Keine Daten")

        try:
            self.extnumberrange.extend(range(self.ext3from, self.ext3to + 1))
        except AttributeError:
            print("Keine Daten")


        # Externe Nummern nach Intern
        for e in self.extnumberrange:
            if self.customerdata["Provider"] == "sbcon":
                e = str(e)
            elif self.customerdata["Provider"] == "combridge":
                e = "0" + str(e)
            for c in range(len(self.convdata)):
                if e[:len(self.convdata[c][0])] == self.convdata[c][0] and self.convdata[c][1] == "0":
                    print("Extern - Intern")
                    self.intnumber = self.convdata[c][0][int(self.convdata[c][4]):] + self.convdata[c][3]
                    self.extnumber = self.convdata[c][0].replace("41", "0", 1)

                    if self.intnumber in self.users:
                        self.users[self.intnumber][10] = str(self.extnumber)

        # Clip nach Extern
        # Clip Daten erstellen
        for i in range(len(self.convdata)):
            if self.convdata[i][1] == "1":
                self.clipdata.append([self.convdata[i][0], self.convdata[i][3], self.convdata[i][4]])

        for d in self.users:
            for c in range(len(self.clipdata)):
                if d[:len(self.clipdata[c][0])] == self.clipdata[c][0]:
                    self.intnumber = d
                    self.extnumber = str(self.clipdata[c][1]) + str(d[int(self.clipdata[c][2]):])
                    self.users[self.intnumber][11] = str(self.extnumber.replace("41", "0", 1))


class Importsystemdata():

    def __init__(self, path):
        self.path = path
        self.systemdata = {}
        self.ts_aboutdata = []
        self.mxone_datadata = []
        self.mgudata = []

    def importsystemdata(self):

        with open(self.path + "/ts_about") as file:
            print("Load Extension File")
            self.ts_aboutdata = file.readlines()
            print(self.ts_aboutdata)
            file.close()

        for i in self.ts_aboutdata:
            if "Version: " in i:
                self.systemdata["mxversion"] = i.partition("Version: ")[2].replace("\n", "", 1)
            elif " MX-ONE Service Node Manager " in i:
                self.systemdata["snmversion"] = i.partition(" MX-ONE Service Node Manager ")[2].replace(" :\n", "", 1)
            elif " MX-ONE Provisioning Manager " in i:
                self.systemdata["pmversion"] = i.partition(" MX-ONE Provisioning Manager ")[2].replace(" :\n", "", 1)


        with open(self.path + "/mxone_data") as file:
            print("Load Extension File")
            self.mxone_datadata = file.readlines()
            print(self.mxone_datadata)
            file.close()

        for i in self.mxone_datadata:
            if "lim" in i:
                i = i.split()
                # 1 ist Hostname, 2 ist IP, 3 ist lim x
                self.systemdata[i[3]] = [i[1], i[2]]
            elif "c-" in i:
                i = i.split()
                # 0 ist Server Name, 1 ist IP des Lims, 3 ist IP der DB
                self.systemdata["Cassandra " + i[0]] = [i[1], i[3]]
        try:
            with open(self.path + "/media_gateway_info_general") as file:
                print("Load Extension File")
                self.mgudata = file.readlines()
                print(self.mgudata)
                file.close()

                gwnumber = 0
                for l in self.mgudata:
                    if " SW information" in l:
                        l = l.split()
                        gwnumber = gwnumber + 1
                        self.systemdata["gateway" + str(gwnumber)] = [l[1]]
                        print("gateway" + str(gwnumber))
                    elif "MGW version: " in l:
                        l = l.split()
                        self.systemdata["gateway" + str(gwnumber)].append(l[2])
                    elif "Media gateway type: " in l:
                        l = l.split()
                        self.systemdata["gateway" + str(gwnumber)].append(l[3] + " " + l[4])
                    elif "Board revision: " in l:
                        l = l.split()
                        self.systemdata["gateway" + str(gwnumber)].append(l[2])
                    elif "Board serial number: " in l:
                        l = l.split()
                        self.systemdata["gateway" + str(gwnumber)].append(l[3])
        except FileNotFoundError:
            print("File Not Found")


class Importsiriodata():

    def __init__(self):
        self.dataEspa = []
        self.dataJob = []
        self.dataCont = []
        self.dataRefEspa = {}
        self.dataRefCont = {}
        self.querydata = {}

        con = fdb.connect(dsn='localhost:c:\sirio.gdb', user='sysdba', password='masterkey')

        cur = con.cursor()

        cur.execute("SELECT AL_ESPA.DESCRIPTION, AL_JOB.JOB_NAME, AL_REF_J.PRI, ALARM.ALARM_NAME "
                    "from AL_ESPA "
                    "right join ALARM on ALARM.ALARM_ID = AL_ESPA.ALARM_ID "
                    "right join AL_REF_A on AL_REF_A.AGROUP_ID = ALARM.AGROUP_ID "
                    "full join AL_REF_J on AL_REF_J.JGROUP_ID = AL_REF_A.JGROUP_ID "
                    "inner join AL_JOB on AL_JOB.JOB_ID = AL_REF_J.JOB_ID "
                    "WHERE ALARM.ALARM_ID = AL_ESPA.ALARM_ID")

        self.dataRefEspa = cur.fetchall()

        cur.execute("SELECT AL_ESPA.DESCRIPTION, AL_JOB.JOB_NAME, AL_REF_J.PRI, ALARM.ALARM_NAME "
                    "from AL_ESPA "
                    "right join ALARM on ALARM.ALARM_ID = AL_ESPA.ALARM_ID "
                    "right join AL_REF_A on AL_REF_A.AGROUP_ID = ALARM.AGROUP_ID "
                    "full join AL_REF_J on AL_REF_J.JGROUP_ID = AL_REF_A.JGROUP_ID "
                    "inner join AL_JOB on AL_JOB.JOB_ID = AL_REF_J.JOB_ID "
                    "WHERE ALARM.ALARM_ID = AL_ESPA.ALARM_ID")

        self.dataRefCont = cur.fetchall()

        cur.execute("select * from AL_ESPA")
        self.dataEspa = cur.fetchall()

        cur.execute("select * from AL_JOB")
        self.dataJob = cur.fetchall()

        cur.execute("select * from AL_AB_IN")
        self.dataCont = cur.fetchall()

        for i in range(len(self.dataRefEspa)):
            if self.dataRefEspa[i][0] in self.querydata:
                self.querydata[self.dataRefEspa[i][0]].append([self.dataRefEspa[i][1], self.dataRefEspa[i][2]])
            else:
                self.querydata[self.dataRefEspa[i][0]] = [[self.dataRefEspa[i][1], self.dataRefEspa[i][2]]]


