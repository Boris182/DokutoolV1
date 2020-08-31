from openpyxl import load_workbook
from datetime import datetime

class Exportmxone():
    def __init__(self, exportpath, customerdata, userdata, systemdata):
        self.exportpath = exportpath
        self.customerdata = customerdata
        self.userdata = userdata
        self.systemdata = systemdata

    def writemxonedata(self):
        # Start Row für Userdaten in der Excel
        self.r = 8
        # Pfad der Vorlage
        self.wbmx = load_workbook("c:/PBX_Doku_Vorlage.xlsx")
        # Sheet auswählen wo die Daten hingeschrieben werden
        self.wsmxuser = self.wbmx['Kundendatenliste']

        # Kundenname
        self.wsmxuser.cell(row=2, column=2).value = self.customerdata["Kundenname"]
        # Datum
        self.wsmxuser.cell(row=2, column=8).value = datetime.now().strftime("%d.%m.%Y")
        # Adresse
        self.wsmxuser.cell(row=3, column=2).value = self.customerdata["Adresse"]
        # Ort
        self.wsmxuser.cell(row=4, column=2).value = self.customerdata["Ort"]
        # Hauptnummer
        self.wsmxuser.cell(row=2, column=5).value = self.customerdata["Hauptnummer"]
        # Faxnummer
        self.wsmxuser.cell(row=3, column=5).value = self.customerdata["Faxnummer"]
        # Nummerbereich 1
        self.wsmxuser.cell(row=2, column=11).value = str(self.customerdata["Nummerbereichfrom1"]) + " - " + str(self.customerdata["Nummerbereichto1"])
        # Nummerbereich 2
        self.wsmxuser.cell(row=3, column=11).value = str(self.customerdata["Nummerbereichfrom2"]) + " - " + str(self.customerdata["Nummerbereichto2"])
        # Nummerbereich 3
        self.wsmxuser.cell(row=4, column=11).value = str(self.customerdata["Nummerbereichfrom3"]) + " - " + str(self.customerdata["Nummerbereichto3"])


        # Schreibt die Userdaten in die Excel Datei
        for i in self.userdata:
            # Number
            self.wsmxuser.cell(row=self.r, column=2).value = self.userdata[i][0]
            # TYP
            self.wsmxuser.cell(row=self.r, column=3).value = self.userdata[i][1]
            # HW Adresse / IP
            self.wsmxuser.cell(row=self.r, column=4).value = self.userdata[i][2]
            # Name 1
            self.wsmxuser.cell(row=self.r, column=7).value = self.userdata[i][3]
            # Name 2
            self.wsmxuser.cell(row=self.r, column=8).value = self.userdata[i][4]
            # Berechtigungen CSP CAT
            self.wsmxuser.cell(row=self.r, column=10).value = self.userdata[i][5]
            # Server
            # self.wsmxuser.cell(row=self.r, column=5).value = self.userdata[i][6]
            # Secondary Dir 1
            self.wsmxuser.cell(row=self.r, column=12).value = self.userdata[i][7]
            # Secondary Dir 2
            self.wsmxuser.cell(row=self.r, column=13).value = self.userdata[i][8]
            # Third
            self.wsmxuser.cell(row=self.r, column=11).value = self.userdata[i][9]

            # Row Plus 1
            self.r = self.r + 1

        #Speichert die Datei als Kopie
        self.wbmx.save(self.exportpath + "/PBX_Doku_" + self.customerdata["Kundenname"] +
                       datetime.now().strftime("%Y%m%d_%I%M%S") + ".xlsx")


class Exportsirio():
    def __init__(self, exportpath, customerdata, refdata, contdata, espadata):
        self.exportpath = exportpath
        self.customerdata = customerdata
        self.refdata = refdata
        self.contdata = contdata
        self.espadata = espadata

    def writesiriodata(self):
        # Pfad der Vorlage
        self.wbsirio = load_workbook("c:/Sirio_Doku_Vorlage.xlsx")
        # Sheet auswählen wo die Daten hingeschrieben werden
        self.wssirio = self.wbmx['Alarmmatrix']

        # Kundenname
        self.wssirio.cell(row=2, column=4).value = self.customerdata["Kundenname"]
        # Datum
        self.wssirio.cell(row=4, column=10).value = datetime.now().strftime("%d.%m.%Y")
        # Adresse
        self.wssirio.cell(row=3, column=4).value = self.customerdata["Adresse"]
        # Ort
        self.wssirio.cell(row=4, column=4).value = self.customerdata["Ort"]




