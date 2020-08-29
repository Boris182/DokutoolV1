from openpyxl import load_workbook

class Exportmxone():
    def __init__(self, exportpath, customerdata, userdata, systemdata):
        self.exportpath = exportpath
        self.customerdata = customerdata
        self.userdata = userdata
        self.systemdata = systemdata


    def writemxonedata(self):
        print("Write MX-One Data")

data = Exportmxone("Test", [3, 3, 5, 6], 4, 6)
data.writemxonedata()