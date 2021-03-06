import fdb

# Klasse für die MX-One Userdaten zu importieren und sortieren
class Importuserdata():

    def __init__(self, path, customerdata):
        self.users = {}
        self.path = path
        self.extensiondata = []
        self.name1datain = []
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
        self.nameinfo = ""

    # Funktion um die Users zu printen die bereits erstellt wurden
    def print_users(self):
        for i in self.users:
            print(self.users[i])

    # Hauptfunktion um die Daten zu laden
    def importuserdata(self):

        # Generic Extensions
        with open(self.path + "/extension") as file:
            print("Load Extension File")
            self.extensiondata = file.readlines()
            print(self.extensiondata[0])
            file.close()

        # Names, es muss per Charakter Index gearbeitet werden, da manche nur einen Name haben
        with open(self.path + "/name1", encoding='utf-8') as file:
            print("Load Extension File")
            self.name1datain = file.readlines()

            # Wenn Priority in der Zeile steht, wird von dieser der Char Index ausgelesen der Spalten
            for i in range(len(self.name1datain)):
                if "Priority" in self.name1datain[i]:
                    self.nameinfo = self.name1datain[i]
                    print(self.nameinfo)

            # Hier wird der Index in eine Variable gespeichert der einzelnen Spalten
            tonumpos = self.nameinfo.find("Number")
            topriopos = self.nameinfo.find("Priority")
            torestpos = self.nameinfo.find("Restriction")
            toname1pos = self.nameinfo.find("Name1")
            toname2pos = self.nameinfo.find("Name2")
            toinfopos = self.nameinfo.find("Info")
            file.close()

            # Nur wenn die Zeile mit einer Zahl Anfängt führe weiteres aus
            # Es wird der Anfangsindex und der Endindex der Line angegeben um die Spalte zu definieren
            for i in range(len(self.name1datain)):
                if self.name1datain[i][0].isdigit():
                    # Number
                    extension = self.name1datain[i][:tonumpos].strip()
                    print(extension)
                    # Number Type
                    numbertype = self.name1datain[i][tonumpos:topriopos].strip()
                    # Prio
                    priority = self.name1datain[i][topriopos:torestpos].strip()
                    # Restriction
                    restriction = self.name1datain[i][torestpos:toname1pos].strip()
                    # Name 1
                    name1 = self.name1datain[i][toname1pos:toname2pos].strip()
                    # Name 2
                    name2 = self.name1datain[i][toname2pos:toinfopos].strip()
                    # Info
                    info = self.name1datain[i][toinfopos:].strip()
                    # Befüllt das neue Array
                    self.name1data.append([extension, numbertype, priority, restriction, name1, name2, info])

        # Dect Extensions
        with open(self.path + "/dect_extension") as file:
            print("Load Extension File")
            self.dect_extensiondata = file.readlines()
            print(self.dect_extensiondata[0])
            file.close()

        # IP Extensions
        with open(self.path + "/ip_extension") as file:
            print("Load Extension File")
            self.ip_extensiondata = file.readlines()
            print(self.ip_extensiondata[0])
            file.close()

        # Analoge Extensions
        with open(self.path + "/EXDDP") as file:
            print("Load Extension File")
            self.exddpdata = file.readlines()
            print(self.exddpdata[0])
            file.close()

        # Digitale Extensions
        with open(self.path + "/KSDDP") as file:
            print("Load Extension File")
            self.ksddpdata = file.readlines()
            print(self.ksddpdata[0])
            file.close()

        # Parallel Ringing Daten
        with open(self.path + "/parallel_ringing") as file:
            print("Load Extension File")
            self.parallel_ringingdata = file.readlines()
            print(self.parallel_ringingdata[0])
            file.close()

        # Nummerumsetzung Daten
        with open(self.path + "/number_conversion_print") as file:
            self.nucondata = file.readlines()
            toentrypos = self.nucondata[1].find("Cnvtyp")
            tocnvtyppos = self.nucondata[1].find("Numtyp")
            tonumtyppos = self.nucondata[1].find("Rou")
            totardestpos = self.nucondata[1].find("Pre")
            toprepos = self.nucondata[1].find("Trc")
            totrcpos = self.nucondata[1].find("Newtyp")

            # Für die Doku werden nicht alle eile Gebraucht, daher sind viele als Reserve
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
                    # Leere Felder werden mit einem 0 Befüllt, da sonst kein Index daraus gemacht werden kann
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

        # Befüllen des User Dictionary

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
        print(self.name1data)
        for i in range(len(self.name1data)):
            if self.name1data[i][0].isdigit():
                userdata = self.name1data[i]

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
                    if len(self.users[number][1]) == 1:
                        self.users[number][1] = "DECT"
                    else:
                        self.users[number][1] = self.users[number][1] + " DECT"
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
                    if len(self.users[number][1]) == 1:
                        self.users[number][1] = iptype
                    else:
                        self.users[number][1] = self.users[number][1] + " " + iptype

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
        # Externe Nummer wird geprüft, ob eine Regel zutrifft
        # Convdata[xy][1] = 0 heisst Extern nach Intern
        for e in self.extnumberrange:
            # Prüft welcher Provider, damit 0 hinzugefügt wird oder nicht
            if self.customerdata["Provider"] == "sbcon":
                e = str(e)
            elif self.customerdata["Provider"] == "combridge":
                e = "0" + str(e)
            # Prüft alle Regeln mit allen Externen Nummern durch
            for c in range(len(self.convdata)):
                # Wenn von der Regel die länge der Entry Daten und die gleiche länge der Externen Nummer
                # übereinstimmt, wird mit den Truncate und Pre Daten die Interne Nummer gerausgefunden
                # Convdata[xy][4] Sind Anzahl Stellen die abgeschnitten werden
                # Convdata[xy][3] Sind die Digits die hinzugefügt werden
                if e[:len(self.convdata[c][0])] == self.convdata[c][0] and self.convdata[c][1] == "0":
                    self.intnumber = self.convdata[c][0][int(self.convdata[c][4]):] + self.convdata[c][3]
                    # Zur korrekten Darstellung wird wenn es mit 41 Anfängt durch 0 ersetzt
                    self.extnumber = self.convdata[c][0].replace("41", "0", 1)
                    # Füllt die Externe Nummer in den vorhandenen Eintrag
                    # Wenn nicht wird nichts gemacht
                    if self.intnumber in self.users:
                        self.users[self.intnumber][10] = str(self.extnumber)

        # Clip nach Extern
        # Interne Nummer wird geprüft, ob eine Regel zutrifft
        # Convdata[xy][1] = 1 heisst Intern nach Extern
        for i in range(len(self.convdata)):
            if self.convdata[i][1] == "1":
                self.clipdata.append([self.convdata[i][0], self.convdata[i][3], self.convdata[i][4]])

        for d in self.users:
            for c in range(len(self.clipdata)):
                # Wenn von der Regel die länge der Entry Daten und die gleiche länge der Internen Nummer
                # übereinstimmt, wird mit den Truncate und Pre Daten die Externe Nummer gerausgefunden
                # clipdata[xy][0] Sind Anzahl Stellen die abgeschnitten werden
                # clipdata[xy][2] Sind die Digits die hinzugefügt werden
                if d[:len(self.clipdata[c][0])] == self.clipdata[c][0]:
                    self.intnumber = d
                    self.extnumber = str(self.clipdata[c][1]) + str(d[int(self.clipdata[c][2]):])
                    # Zur korrekten Darstellung wird wenn es mit 41 Anfängt durch 0 ersetzt
                    self.users[self.intnumber][11] = str(self.extnumber.replace("41", "0", 1))


class Importsystemdata():

    def __init__(self, path):
        self.path = path
        self.systemdata = {}
        self.ts_aboutdata = []
        self.mxone_datadata = []
        self.mgudata = []

    def importsystemdata(self):
        # Software Version wird geladen
        with open(self.path + "/ts_about") as file:
            print("Load ts_about File")
            self.ts_aboutdata = file.readlines()
            print(self.ts_aboutdata)
            file.close()

        # Alle Lines werden durchgegangen und nach Keyword gesucht
        # Wenn Keyword gefunden, wird gesplittet und Daten in Dictionary geladen
        for i in self.ts_aboutdata:
            if "Version: " in i:
                self.systemdata["mxversion"] = i.partition("Version: ")[2].replace("\n", "", 1)
            elif " MX-ONE Service Node Manager " in i:
                self.systemdata["snmversion"] = i.partition(" MX-ONE Service Node Manager ")[2].replace(" :\n", "", 1)
            elif " MX-ONE Provisioning Manager " in i:
                self.systemdata["pmversion"] = i.partition(" MX-ONE Provisioning Manager ")[2].replace(" :\n", "", 1)

        # Es werden IP Adressen und Namen des Systems geladen
        with open(self.path + "/mxone_data") as file:
            print("Load mxone_data File")
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

        # Es werden alle Mediagateway Daten geladen, wenn solche existieren
        try:
            with open(self.path + "/media_gateway_info_general") as file:
                print("Load media_gateway_info File")
                self.mgudata = file.readlines()
                print(self.mgudata)
                file.close()

                # Wenn mehrere Gateway bestehen werde die Gateways mit Nummern versehen
                # Start Nummer 0 damit das erste Gateway 1 bekommt
                gwnumber = 0
                for l in self.mgudata:
                    # Wenn eine Line das Keyword enthält wird ein Gateway + 1 erstellt
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
            print("Media Gateway General existiert nicht")


class Importsiriodata():

    def __init__(self, path):
        self.dataEspa = []
        self.dataJob = []
        self.dataCont = []
        self.dataRefEspa = {}
        self.dataRefCont0 = {}
        self.dataRefCont1 = {}
        self.querydata = {}
        self.path = path

        # Verbindung zum Datenbank File
        con = fdb.connect(dsn='localhost:' + path, user='sysdba', password='masterkey')
        # Erstellung des Cursor für die Absetzung der SQL befehle
        cur = con.cursor()

        # Referenz Daten der ESPA Alarme
        cur.execute("SELECT AL_ESPA.DESCRIPTION, AL_JOB.JOB_NAME, AL_REF_J.PRI, ALARM.ALARM_NAME "
                    "from AL_ESPA "
                    "right join ALARM on ALARM.ALARM_ID = AL_ESPA.ALARM_ID "
                    "right join AL_REF_A on AL_REF_A.AGROUP_ID = ALARM.AGROUP_ID "
                    "full join AL_REF_J on AL_REF_J.JGROUP_ID = AL_REF_A.JGROUP_ID "
                    "inner join AL_JOB on AL_JOB.JOB_ID = AL_REF_J.JOB_ID "
                    "WHERE ALARM.ALARM_ID = AL_ESPA.ALARM_ID")

        self.dataRefEspa = cur.fetchall()

        # Referenz Daten der Eingangskontaktdaten bei NC
        cur.execute("SELECT AL_AB_IN.C_NAME, AL_JOB.JOB_NAME, AL_REF_J.PRI, ALARM.ALARM_NAME "
                    "from AL_AB_IN "
                    "right join ALARM on ALARM.ALARM_ID = AL_AB_IN.ALARM_ID_0 "
                    "right join AL_REF_A on AL_REF_A.AGROUP_ID = ALARM.AGROUP_ID "
                    "full join AL_REF_J on AL_REF_J.JGROUP_ID = AL_REF_A.JGROUP_ID "
                    "inner join AL_JOB on AL_JOB.JOB_ID = AL_REF_J.JOB_ID "
                    "WHERE ALARM.ALARM_ID = AL_AB_IN.ALARM_ID_0")

        self.dataRefCont0 = cur.fetchall()

        # Referenz Daten der Eingangskontaktdaten bei NO
        cur.execute("SELECT AL_AB_IN.C_NAME, AL_JOB.JOB_NAME, AL_REF_J.PRI, ALARM.ALARM_NAME "
                    "from AL_AB_IN "
                    "right join ALARM on ALARM.ALARM_ID = AL_AB_IN.ALARM_ID_1 "
                    "right join AL_REF_A on AL_REF_A.AGROUP_ID = ALARM.AGROUP_ID "
                    "full join AL_REF_J on AL_REF_J.JGROUP_ID = AL_REF_A.JGROUP_ID "
                    "inner join AL_JOB on AL_JOB.JOB_ID = AL_REF_J.JOB_ID "
                    "WHERE ALARM.ALARM_ID = AL_AB_IN.ALARM_ID_1")

        self.dataRefCont1 = cur.fetchall()

        # ESPA Alarm Daten
        cur.execute("select * from AL_ESPA")
        self.dataEspa = cur.fetchall()

        # Teilnehmer Daten
        cur.execute("select * from AL_JOB")
        self.dataJob = cur.fetchall()

        # Eingandskontaktdaten
        cur.execute("select * from AL_AB_IN")
        self.dataCont = cur.fetchall()

        # Es wird für jeden Alarm geschsaut, welche Teilnehmer diesen Alarm erhalten
        # Es wird ein Dictionary erstellt, in dem für ein Alarm als Keyword
        # alle Teilnehmer als Listen enthalten sind
        for i in range(len(self.dataRefEspa)):
            # Wenn es den Eintrag schon gibt, füge einen weiteren Teilnehmer hinzu
            if self.dataRefEspa[i][0] in self.querydata:
                self.querydata[self.dataRefEspa[i][0]].append([self.dataRefEspa[i][1], self.dataRefEspa[i][2]])
            # Wenn es den Eintrag noch nicht gibt, erstelle einen neuen und füge den Teilnehmer hinzu
            else:
                self.querydata[self.dataRefEspa[i][0]] = [[self.dataRefEspa[i][1], self.dataRefEspa[i][2]]]

        for i in range(len(self.dataRefCont0)):
            # Wenn es den Eintrag schon gibt, füge einen weiteren Teilnehmer hinzu
            if self.dataRefCont0[i][0] in self.querydata:
                self.querydata[self.dataRefCont0[i][0]].append([self.dataRefCont0[i][1], self.dataRefCont0[i][2]])
            # Wenn es den Eintrag noch nicht gibt, erstelle einen neuen und füge den Teilnehmer hinzu
            else:
                self.querydata[self.dataRefCont0[i][0]] = [[self.dataRefCont0[i][1], self.dataRefCont0[i][2]]]

        for i in range(len(self.dataRefCont1)):
            # Wenn es den Eintrag schon gibt, füge einen weiteren Teilnehmer hinzu
            if self.dataRefCont1[i][0] in self.querydata:
                self.querydata[self.dataRefCont1[i][0]].append([self.dataRefCont1[i][1], self.dataRefCont1[i][2]])
            # Wenn es den Eintrag noch nicht gibt, erstelle einen neuen und füge den Teilnehmer hinzu
            else:
                self.querydata[self.dataRefCont1[i][0]] = [[self.dataRefCont1[i][1], self.dataRefCont1[i][2]]]

