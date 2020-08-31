import importdata
import testexcel

customerdata = {"Kundenname": "00325-Parcom", "Adresse": "Hasliring 1", "Ort": "6032 Emmen"}

#siriodata = importdata.Importsiriodata()
mxonedata = importdata.Importuserdata("C:/Source20200821")

mxonedata.importuserdata()
mxonedata.createuserdata()
mxonedata.print_users()
#print(mxonedata.users)
#print(customerdata)

mxoneexport = testexcel.Exportmxone("C:/", customerdata, mxonedata.users, "Systemdata")
#mxoneexport.printmxonedata()
mxoneexport.writemxonedata()






#siriodata.createevents()
