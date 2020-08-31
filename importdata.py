import fdb

class Importuserdata():

    def __init__(self, path):
        self.users = {}
        self.path = path
        self.extensiondata = []
        self.name1data = []
        self.dect_extensiondata = []
        self.ip_extensiondata = []
        self.exddpdata = []
        self.ksddpdata = []
        self.parallel_ringingdata = []
        self.users = {}

    def print_users(self):
        for i in self.users:
            print(self.users[i])

    def importuserdata(self):

        with open(self.path + "/extension") as file:
            print("Load Extension File")
            self.extensiondata = file.readlines()
            print(self.extensiondata[0])

        with open(self.path + "/name1", encoding='utf-8') as file:
            print("Load Extension File")
            self.name1data = file.readlines()
            print(self.name1data[0])

        with open(self.path + "/dect_extension") as file:
            print("Load Extension File")
            self.dect_extensiondata = file.readlines()
            print(self.dect_extensiondata[0])

        with open(self.path + "/ip_extension") as file:
            print("Load Extension File")
            self.ip_extensiondata = file.readlines()
            print(self.ip_extensiondata[0])

        with open(self.path + "/EXDDP") as file:
            print("Load Extension File")
            self.exddpdata = file.readlines()
            print(self.exddpdata[0])

        with open(self.path + "/KSDDP") as file:
            print("Load Extension File")
            self.ksddpdata = file.readlines()
            print(self.ksddpdata[0])

        with open(self.path + "/parallel_ringing") as file:
            print("Load Extension File")
            self.parallel_ringingdata = file.readlines()
            print(self.parallel_ringingdata[0])

    #Erstellt und Sortiert das User Dictionary, fügt alle Dateien zusammen und ergänzt diese
    def createuserdata(self):
        # Erstellen des User Dictionary

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

        for i in range(len(self.parallel_ringingdata)):
            if self.parallel_ringingdata[i][0].isdigit():
                userdata = self.parallel_ringingdata[i].split()

                number = str(userdata[0])
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

class Importsystemdata():

    def __init__(self, path):
        self.path = path
        self.system = {}
        self.ts_aboutdata = []

    def importsystemdata(self):

        with open(self.path + "/ts_about") as file:
            print("Load Extension File")
            self.ts_aboutdata = file.readlines()
            print(self.ts_aboutdata[0])

class Importsiriodata():

    def __init__(self):
        con = fdb.connect(dsn='localhost:c:\sirio.gdb', user='sysdba', password='masterkey')

        cur = con.cursor()

        cur.execute("select * from ALARM")
        self.dataAlarm = cur.fetchall()

        cur.execute("select * from AL_ESPA")
        self.dataEspa = cur.fetchall()

        cur.execute("select * from AL_JOB")
        self.dataJob = cur.fetchall()

        cur.execute("select * from AL_AB_IN")
        self.dataCont = cur.fetchall()

        print(self.dataAlarm)
        print(self.dataEspa)
        print(self.dataJob)
        print(self.dataCont)





