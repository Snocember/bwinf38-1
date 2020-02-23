# -*- coding: utf8 -*-
#!/usr/bin/env python3
# python3.7.0
# (c) Snocember, 2019
# BWINF 2019, Aufgabe Parallelen

# ----#---- Importe und Initialisierungen ----#----
import sys # sys.exit() falls datei nicht gefunden.
gelb = '\033[30;103m'
pink = '\033[30;105m'
cyan = "\033[96m"
reset = "\033[0m"
gedicht = []
zahlen = []
sonderz = ".,:;?!–\n"

print()
print("Das Programm erfordert für ein angenehmes Bedienen eine Terminal-Umgebung mit ANSI-Farbunterstützung.")
print(cyan)
print(" ______                _ _      _             ")
print(" |  __ \              | | |    | |           ")
print(" | |__) |_ _ _ __ __ _| | | ___| | ___ _ __  ")
print(" |  ___/ _` | '__/ _` | | |/ _ \ |/ _ \ '_ \ ")
print(" | |  | (_| | | | (_| | | |  __/ |  __/ | | |")
print(" |_|   \__,_|_|  \__,_|_|_|\___|_|\___|_| |_|")
print(reset)

# ----#----#---- EINLESEN ----#----
try:
    file = open("./parallelen.txt")

    inhalt = file.readlines()
    groesse = len(inhalt)
    for i in range(0, groesse):
        text = inhalt[i].split()
        anzahl2 = len(text)
        for u in range(0, anzahl2):
            splittext = text[u]
            for x in sonderz:
                splittext = splittext.replace(x,"")
            gedicht.append(splittext)
            zahlen.append(len(splittext))
except FileNotFoundError:
    print("ES WURDE DIE DATEI ZUM EINLESEN NICHT GEFUNDEN. DAS PROGRAMM BENÖTIGT 'parallelen.txt' IM SELBEN VERZEICHNIS.")
    print("QUELLE ZUM HERUNTERLADEN: https://bwinf.de/fileadmin/user_upload/BwInf/2019/38/1._Runde/Material/J1/parallelen.txt")
    print()
    sys.exit(0)

gedicht.remove("")
print(pink+"EINGABE"+reset+" (Original vom der BWINF-Website, bereits hier vom Programm bearbeitet, sodass keine Satz- und Sonderzeichen vorkommen.)")
print()
print(gedicht)
print()
print("Die Hälfte des Gedichts endet, wie vorgeschrieben, bei: 'Doch als sie zehn Lichtjahre gewandert neben sich hin,'.")
print()
#print(zahlen)
# ----#----#---- AUSWERTEN----#----
print(pink+"AUSWERTUNG"+reset)
index = gedicht.index("hin")
nein = 0
endwort = ""
schleife = True

for x in range(0,index+1):
    lettern = len(gedicht[x]) #verändert
    print(gedicht[x]+"("+str(lettern)+") ", end=" ")
    OK = True
    count = 0+lettern
    while OK:
        try:
            newwort = gedicht[x+count]
            lettern = len(gedicht[x+count])
            print("->"+newwort+"("+str(lettern)+")", end=" ")
            count = count+lettern
            #print(count, end=" ")
        except IndexError:
            if x == 0:
                    endwort = newwort
            if newwort != endwort:
                nein = 1
                print("ANDERES ENDWORT: "+newwort, end=" ")
                schleife = False
            print()
            print("Endwort nach diesem Durchgang: "+gelb+newwort+reset)
            break
    if schleife == False:
        break
# ----#----#---- ERGEBNIS ----#----
print(cyan+"-----------------------------"+pink+"ERGEBNIS"+reset+cyan+"-----------------------------"+reset)
if nein == 0:
    print("Martin "+pink+"HAT RECHT!"+reset)
    print("Das Endwort nach jedem Durchgang (bis zur Hälfte des Gedichts) war: "+gelb+endwort+reset)
if nein != 0:
    print("Martin "+pink+"hat NICHT Recht!"+reset)
    print("Die Endwörter nach jedem Durchgang (bis zur Hälfte des Gedichts) war verschieden.")
print("------------------------------------------------------------------")
