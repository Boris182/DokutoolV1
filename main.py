from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import importdata
import exportdata

root = Tk()
root.title("MX-Dokumentationstool")


mxonepath = ""
siriopath = ""

mxoneoutput = ""
siriooutput = ""

mxoneversion = StringVar()
mxoneversion.set("Select Version")

provider = StringVar()
provider.set("Select Provider")

sirioversion = StringVar()
sirioversion.set("Select Version")


# Funktionen
def openmxonedir():
    global mxonepath
    mxonepath = filedialog.askdirectory(initialdir="c:/")
    labelPathMxone = Label(frameMxone, text="Path: " + mxonepath)
    labelPathMxone.grid(row=3, column=0)
    return mxonepath


def opensiriofile():
    global siriopath
    siriopath = filedialog.askopenfilename(initialdir="c:/")
    labelPathSirio = Label(frameSirio, text="Path: " + siriopath)
    labelPathSirio.grid(row=3, column=0)
    return siriopath


def outputmxonedir():
    global mxoneoutput
    mxoneoutput = filedialog.askdirectory(initialdir="c:/")
    labelOutputMxone = Label(frameMxone, text="Path: " + mxoneoutput)
    labelOutputMxone.grid(row=6, column=0)
    return mxoneoutput


def outputsiriodir():
    global siriooutput
    siriooutput = filedialog.askdirectory(initialdir="c:/")
    labelOutputSirio = Label(frameSirio, text="Path: " + siriooutput)
    labelOutputSirio.grid(row=6, column=0)
    return siriooutput


def checkmxonefiles():
    response = messagebox.askyesno("Kontrolle der Daten",
                                   "Kundenname: " + str(inputKundenname.get()) + "\n" +
                                   "Adresse: " + str(inputAdresse.get()) + "\n" +
                                   "Ort: " + str(inputOrt.get()) + "\n" +
                                   "Hauptnummer: " + str(inputHauptnummer.get()) + "\n" +
                                   "Faxnummer: " + str(inputFaxnummer.get()) + "\n" +
                                   "Nummerbereich 1: " + str(inputExternalFrom1.get()) + " - " +
                                   str(inputExternalTo1.get()) + "\n" +
                                   "Nummerbereich 2: " + str(inputExternalFrom2.get()) + " - " +
                                   str(inputExternalTo2.get()) + "\n" +
                                   "Nummerbereich 3: " + str(inputExternalFrom3.get()) + " - " +
                                   str(inputExternalTo3.get()) + "\n" +
                                   "Ausgabeverzeichnis: " + str(mxoneoutput) + "\n" +
                                   "Provider: " + str(provider.get()) + "\n" + "\n" +
                                   "Sind Sie sich sicher? Stimmen die Daten?")
    if response == 1:
        print("Es wird ausgeführt")
    else:
        print("Abbruch")


def createmxonedoc():
    response = messagebox.askyesno("Kontrolle der Daten",
                                   "Kundenname: " + str(inputKundenname.get()) + "\n" +
                                   "Adresse: " + str(inputAdresse.get()) + "\n" +
                                   "Ort: " + str(inputOrt.get()) + "\n" +
                                   "Hauptnummer: " + str(inputHauptnummer.get()) + "\n" +
                                   "Faxnummer: " + str(inputFaxnummer.get()) + "\n" +
                                   "Nummerbereich 1: " + str(inputExternalFrom1.get()) + " - " +
                                   str(inputExternalTo1.get()) + "\n" +
                                   "Nummerbereich 2: " + str(inputExternalFrom2.get()) + " - " +
                                   str(inputExternalTo2.get()) + "\n" +
                                   "Nummerbereich 3: " + str(inputExternalFrom3.get()) + " - " +
                                   str(inputExternalTo3.get()) + "\n" +
                                   "Ausgabeverzeichnis: " + str(mxoneoutput) + "\n" +
                                   "Provider: " + str(provider.get()) + "\n" + "\n" +
                                   "Sind Sie sich sicher? Stimmen die Daten?")
    if response == 1:
        customerdata = {"Kundenname": inputKundenname.get(),
                        "Adresse": inputAdresse.get(),
                        "Ort": inputOrt.get(),
                        "Hauptnummer": inputHauptnummer.get(),
                        "Faxnummer": inputFaxnummer.get(),
                        "Nummerbereichfrom1": inputExternalFrom1.get(),
                        "Nummerbereichto1": inputExternalTo1.get(),
                        "Nummerbereichfrom2": inputExternalFrom2.get(),
                        "Nummerbereichto2": inputExternalTo2.get(),
                        "Nummerbereichfrom3": inputExternalFrom3.get(),
                        "Nummerbereichto3": inputExternalTo3.get(),
                        "Provider": provider.get()}

        mxoneuserdata = importdata.Importuserdata(mxonepath, customerdata)
        mxoneuserdata.importuserdata()
        mxoneuserdata.createuserdata()

        mxonesystemdata = importdata.Importsystemdata(mxonepath)
        mxonesystemdata.importsystemdata()

        mxoneexport = exportdata.Exportmxone(mxoneoutput,
                                             customerdata,
                                             mxoneuserdata.users,
                                             mxonesystemdata.systemdata,
                                             mxoneuserdata.extnumberrange)
        mxoneexport.writemxonedata()
        messagebox.showinfo("Finish", "Die Doku wurde erfolgreich generiert")
    else:
        print("Abbruch")


def checksiriofile():
    response = messagebox.askyesno("Kontrolle der Daten",
                                   "Kundenname: " + inputKundenname.get() + "\n" +
                                   "Adresse: " + inputAdresse.get() + "\n" +
                                   "Ort: " + inputOrt.get() + "\n" +
                                   "Sind Sie sich sicher? Stimmen die Daten?")
    if response == 1:
        print("Es wird ausgeführt")
    else:
        print("Abbruch")


def createsiriodoc():
    response = messagebox.askyesno("Kontrolle der Daten",
                                   "Kundenname: " + inputKundenname.get() + "\n" +
                                   "Adresse: " + inputAdresse.get() + "\n" +
                                   "Ort: " + inputOrt.get() + "\n" +
                                   "Ausgabeverzeichnis: " + siriooutput + "\n" + "\n" +
                                   "Sind Sie sich sicher? Stimmen die Daten?")
    if response == 1:
        customerdata = {"Kundenname": inputKundenname.get(),
                        "Adresse": inputAdresse.get(),
                        "Ort": inputOrt.get()}

        siriodata = importdata.Importsiriodata(siriopath)

        sirioexport = exportdata.Exportsirio(siriooutput,
                                             customerdata,
                                             siriodata.querydata,
                                             siriodata.dataCont,
                                             siriodata.dataEspa,
                                             siriodata.dataJob)
        sirioexport.writesiriodata()
        messagebox.showinfo("Finish", "Die Doku wurde erfolgreich generiert")

    else:
        print("Abbruch")


# Frames initiieren
frameInfo = LabelFrame(root, text="Info", padx=5, pady=5)
frameInfo.grid(row=0, column=0, padx=5, pady=5)
frameKundendaten = LabelFrame(root, text="Kundendaten", padx=5)
frameKundendaten.grid(row=1, column=0, padx=5, pady=5)
frameNumberdata = LabelFrame(root, text="Nummerbereich Extern", padx=5, pady=5)
frameNumberdata.grid(row=2, column=0, padx=5, pady=5)
frameMxone = LabelFrame(root, text="MX-One", padx=5, pady=5)
frameMxone.grid(row=0, rowspan=3, sticky=N, column=1, padx=5, pady=5)
frameSirio = LabelFrame(root, text="Sirio", padx=5, pady=5)
frameSirio.grid(row=0, rowspan=3, sticky=N, column=2, padx=5, pady=5)

# Info Frame-------------------------------------------------------
labelInfo = Label(frameInfo, text="Bitte trage die Daten des Kunden sorgfältig ein\n"
                                  "Für die MX-One ist der Nummerbereich wichtig damit\n"
                                  "die Nummerumsetzung richtig funktioniert.\n"
                                  "Viel Spass :-)")
labelInfo.grid()

# Kundendaten Frame-------------------------------------------------

# Labels
labelKundenname = Label(frameKundendaten, text="Kundenname: ")
labelKundenname.grid(row=0, column=0)
labelAdresse = Label(frameKundendaten, text="Adresse: ")
labelAdresse.grid(row=1, column=0)
labelOrt = Label(frameKundendaten, text="PLZ Ort: ")
labelOrt.grid(row=2, column=0)
labelHauptnummer = Label(frameKundendaten, text="Hauptnummer: ")
labelHauptnummer.grid(row=3, column=0)
labelFaxnummer = Label(frameKundendaten, text="Faxnummer: ")
labelFaxnummer.grid(row=4, column=0)

# Input Felder
inputKundenname = Entry(frameKundendaten, borderwidth=2, width=30)
inputKundenname.grid(row=0, column=1)
inputAdresse = Entry(frameKundendaten, borderwidth=2, width=30)
inputAdresse.grid(row=1, column=1)
inputOrt = Entry(frameKundendaten, borderwidth=2, width=30)
inputOrt.grid(row=2, column=1)
inputHauptnummer = Entry(frameKundendaten, borderwidth=2, width=30)
inputHauptnummer.grid(row=3, column=1)
inputFaxnummer = Entry(frameKundendaten, borderwidth=2, width=30)
inputFaxnummer.grid(row=4, column=1)

# Nummerbereich Frame------------------------------------------------

# Labels
labelFrom = Label(frameNumberdata, text="Von", width=20).grid(row=0, column=0)
labelTo = Label(frameNumberdata, text="Bis", width=20).grid(row=0, column=1)

# Input Felder
inputExternalFrom1 = Entry(frameNumberdata, width=20, borderwidth=2)
inputExternalFrom1.grid(row=1, column=0)
inputExternalTo1 = Entry(frameNumberdata, width=20, borderwidth=2)
inputExternalTo1.grid(row=1, column=1)
inputExternalFrom2 = Entry(frameNumberdata, width=20, borderwidth=2)
inputExternalFrom2.grid(row=2, column=0)
inputExternalTo2 = Entry(frameNumberdata, width=20, borderwidth=2)
inputExternalTo2.grid(row=2, column=1)
inputExternalFrom3 = Entry(frameNumberdata, width=20, borderwidth=2)
inputExternalFrom3.grid(row=3, column=0)
inputExternalTo3 = Entry(frameNumberdata, width=20, borderwidth=2)
inputExternalTo3.grid(row=3, column=1)

# MX-One Frame-------------------------------------

# Labels
labelInfoMxone = Label(frameMxone, text="Bitte wähle das Verzeichniss der Source Files der MX-One. \n "
                                        "Wähle den Provider korrekt aus, ansonsten funktioniert die \n"
                                        "Nummerumsetzung nicht\n"
                                        "Danach kann mit ""Create"" die Dokumentation erstellt werden").grid(row=0, column=0)
labelInfoPathMxone = Label(frameMxone, text="Wähle das Verzeichniss der REGEN Files").grid(row=1, column=0)
labelPathMxone = Label(frameMxone, text="Path: " + mxonepath).grid(row=3, column=0)
labelInfoOutputMxone = Label(frameMxone, text="Wähle das Output Verzeichniss").grid(row=4, column=0)
labelOutputMxone = Label(frameMxone, text="Path: " + mxoneoutput).grid(row=6, column=0)

# Buttons
buttonPfadMxone = Button(frameMxone, text="Browse", width=30, command=openmxonedir)
buttonPfadMxone.grid(row=2, column=0)
buttonOutputMxone = Button(frameMxone, text="Browse", width=30, command=outputmxonedir)
buttonOutputMxone.grid(row=5, column=0)
buttonCheckMxone = Button(frameMxone, text="Check Files", width=30, command=checkmxonefiles)
buttonCheckMxone.grid(row=8, column=0)
buttonCreateMxone = Button(frameMxone, text="Create", width=30, command=createmxonedoc)
buttonCreateMxone.grid(row=12, column=0)

# Dropdowns
dropMxoneVersion = OptionMenu(frameMxone, mxoneversion, "MX-One 6.X", "MX-One 7.X")
dropMxoneVersion.grid(row=10, column=0)
dropProvider = OptionMenu(frameMxone, provider, "sbcon", "combridge")
dropProvider.grid(row=11, column=0)

# Sirio Frame
# Labels
labelInfoSirio = Label(frameSirio, text="Bitte wähle das .gdp Datenbank File aus.\n"
                                        "Aus dem Datenbank File ensteht danach mit dem\n"
                                        "Create Button die Dokumentation")
labelInfoSirio.grid(row=0, column=0)
labelInfoPathSirio = Label(frameSirio, text="Wähle die Datenbank Datei aus")
labelInfoPathSirio.grid(row=1, column=0)
labelPathSirio = Label(frameSirio, text="Path: " + siriopath)
labelPathSirio.grid(row=3, column=0)
labelInfoOutputSirio = Label(frameSirio, text="Wähle das Output Verzeichniss")
labelInfoOutputSirio.grid(row=4, column=0)
labelOutputSirio = Label(frameSirio, text="Path: " + siriooutput)
labelOutputSirio.grid(row=6, column=0)

# Buttons
buttonPfadSirio = Button(frameSirio, text="Browse", width=30, command=opensiriofile)
buttonPfadSirio.grid(row=2, column=0)
buttonOutputSirio = Button(frameSirio, text="Browse", width=30, command=outputsiriodir)
buttonOutputSirio.grid(row=5, column=0)
buttonCheckSirio = Button(frameSirio, text="Check File", width=30, command=checksiriofile)
buttonCheckSirio.grid(row=8, column=0)
buttonCreateSirio = Button(frameSirio, text="Create", width=30, command=createsiriodoc)
buttonCreateSirio.grid(row=11, column=0)

# Dropdowns
dropSirioVersion = OptionMenu(frameSirio, sirioversion, "V1", "V2")
dropSirioVersion.grid(row=10, column=0)

root.mainloop()
