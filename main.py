from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import importdata

root = Tk()
root.title("MX-Dokumentationstool")

mxonepath = ""
siriopath = ""

mxoneoutput = ""
siriooutput = ""

mxoneversion = StringVar()
mxoneversion.set("Select Version")

sirioversion = StringVar()
sirioversion.set("Select Version")


# Funktionen
def openmxonedir():
    global mxonepath
    mxonepath = filedialog.askdirectory(initialdir="c:/")
    labelPathMxone = Label(frameMxone, text="Path: " + mxonepath).grid(row=3, column=0)
    return mxonepath


def opensiriofile():
    global siriopath
    siriopath = filedialog.askopenfilename(initialdir="c:/")
    labelPathSirio = Label(frameSirio, text="Path: " + siriopath).grid(row=3, column=0)
    return siriopath


def outputmxonedir():
    global mxoneoutput
    mxoneoutput = filedialog.askdirectory(initialdir="c:/")
    labelOutputMxone = Label(frameMxone, text="Path: " + mxoneoutput).grid(row=6, column=0)
    return mxoneoutput


def outputsiriodir():
    global siriooutput
    siriooutput = filedialog.askdirectory(initialdir="c:/")
    labelOutputSirio = Label(frameSirio, text="Path: " + siriooutput).grid(row=6, column=0)
    return siriooutput


def checkmxonefiles():
    response = messagebox.askyesno("Kontrolle der Daten",
                                   "Kundenname: " + inputKundenname.get() + "\n" +
                                   "Adresse: " + inputAdresse.get() + "\n" +
                                   "Ort: " + inputOrt.get() + "\n" +
                                   "Hauptnummer: " + inputHauptnummer.get() + "\n" +
                                   "Faxnummer: " + inputFaxnummer.get() + "\n" +
                                   "Nummerbereich 1: " + inputExternalFrom1.get() +
                                   " - " + inputExternalTo1.get() + "\n" +
                                   "Nummerbereich 2: " + inputExternalFrom2.get() +
                                   " - " + inputExternalTo2.get() + "\n" +
                                   "Nummerbereich 3: " + inputExternalFrom3.get() +
                                   " - " + inputExternalTo3.get() + "\n" +
                                   "Ausgabeverzeichnis: " + mxoneoutput + "\n" + "\n" +
                                   "Sind Sie sich sicher? Stimmen die Daten?")
    if response == 1:
        print("Es wird ausgeführt")
    else:
        print("Abbruch")


def checksiriofile():
    response = messagebox.askyesno("Kontrolle der Daten",
                                   "Kundenname: " + inputKundenname.get() + "\n" +
                                   "Adresse: " + inputAdresse.get() + "\n" +
                                   "Ort: " + inputOrt.get() + "\n" +
                                   "Hauptnummer: " + inputHauptnummer.get() + "\n" +
                                   "Faxnummer: " + inputFaxnummer.get() + "\n" +
                                   "Nummerbereich 1: " + inputExternalFrom1.get() +
                                   " - " + inputExternalTo1.get() + "\n" +
                                   "Nummerbereich 2: " + inputExternalFrom2.get() +
                                   " - " + inputExternalTo2.get() + "\n" +
                                   "Nummerbereich 3: " + inputExternalFrom3.get() +
                                   " - " + inputExternalTo3.get() + "\n" +
                                   "Ausgabeverzeichnis: " + siriooutput + "\n" + "\n" +
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
                                   "Hauptnummer: " + inputHauptnummer.get() + "\n" +
                                   "Faxnummer: " + inputFaxnummer.get() + "\n" +
                                   "Nummerbereich 1: " + inputExternalFrom1.get() + " - " + inputExternalTo1.get() + "\n" +
                                   "Nummerbereich 2: " + inputExternalFrom2.get() + " - " + inputExternalTo2.get() + "\n" +
                                   "Nummerbereich 3: " + inputExternalFrom3.get() + " - " + inputExternalTo3.get() + "\n" +
                                   "Ausgabeverzeichnis: " + siriooutput + "\n" + "\n" +
                                   "Sind Sie sich sicher? Stimmen die Daten?")
    if response == 1:
        siriodata = importdata.Importsiriodata()

    else:
        print("Abbruch")


def createmxonedoc():
    response = messagebox.askyesno("Kontrolle der Daten",
                                   "Kundenname: " + inputKundenname.get() + "\n" +
                                   "Adresse: " + inputAdresse.get() + "\n" +
                                   "Ort: " + inputOrt.get() + "\n" +
                                   "Hauptnummer: " + inputHauptnummer.get() + "\n" +
                                   "Faxnummer: " + inputFaxnummer.get() + "\n" +
                                   "Nummerbereich 1: " + inputExternalFrom1.get() + " - " + inputExternalTo1.get() + "\n" +
                                   "Nummerbereich 2: " + inputExternalFrom2.get() + " - " + inputExternalTo2.get() + "\n" +
                                   "Nummerbereich 3: " + inputExternalFrom3.get() + " - " + inputExternalTo3.get() + "\n" +
                                   "Ausgabeverzeichnis: " + siriooutput + "\n" + "\n" +
                                   "Sind Sie sich sicher? Stimmen die Daten?")
    if response == 1:
        mxonedata = importdata.Importuserdata(mxonepath)
        mxonedata.importuserdata()
        mxonedata.createuserdata()
        mxonedata.print_users()
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
labelInfo = Label(frameInfo, text="Das ist die Info").grid()

# Kundendaten Frame-------------------------------------------------

# Labels
labelKundenname = Label(frameKundendaten, text="Kundenname: ").grid(row=0, column=0)
labelAdresse = Label(frameKundendaten, text="Adresse: ").grid(row=1, column=0)
labelOrt = Label(frameKundendaten, text="PLZ Ort: ").grid(row=2, column=0)
labelHauptnummer = Label(frameKundendaten, text="Hauptnummer: ").grid(row=3, column=0)
labelFaxnummer = Label(frameKundendaten, text="Faxnummer: ").grid(row=4, column=0)

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
labelInfoMxone = Label(frameMxone, text="Hier entsteht die MX-One Konfig").grid(row=0, column=0)
labelInfoPathMxone = Label(frameMxone, text="Wähle das Verzeichniss der REGEN Files").grid(row=1, column=0)
labelPathMxone = Label(frameMxone, text="Path: " + mxonepath).grid(row=3, column=0)
labelInfoOutputMxone = Label(frameMxone, text="Wähle das Output Verzeichniss").grid(row=4, column=0)
labelOutputMxone = Label(frameMxone, text="Path: " + mxoneoutput).grid(row=6, column=0)

# Buttons
buttonPfadMxone = Button(frameMxone, text="Browse", width=30, command=openmxonedir).grid(row=2, column=0)
buttonOutputMxone = Button(frameMxone, text="Browse", width=30, command=outputmxonedir).grid(row=5, column=0)
buttonCheckMxone = Button(frameMxone, text="Check Files", width=30, command=checkmxonefiles).grid(row=8, column=0)
buttonCreateMxone = Button(frameMxone, text="Create", width=30, command=createmxonedoc)
buttonCreateMxone.grid(row=11, column=0)

# Dropdowns
dropMxoneVersion = OptionMenu(frameMxone, mxoneversion, "MX-One 6.X", "MX-One 7.X")
dropMxoneVersion.grid(row=10, column=0)

# Sirio Frame
# Labels
labelInfoSirio = Label(frameSirio, text="Hier entsteht die Sirio Konfig")
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
