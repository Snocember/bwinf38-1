# -*- coding: utf8 -*-
# python3.7.0
# (c) Snocember, 2019
# BWINF 2019, Aufgabe Nummernmerker

# ----#---- Importe und Initialisierungen ----#----
import sys # sys.exit() falls datei nicht gefunden.
cyan = "\033[96m"
pink = '\033[30;105m'
gelb = '\033[93m'
reset = "\033[0m"

print()
print("Das Programm erfordert für ein angenehmes Bedienen eine Terminal-Umgebung mit ANSI-Farbunterstützung.")
print(cyan+"  _   _                                                               _             ")
print(" | \ | |                                                             | |            ")
print(" |  \| |_   _ _ __ ___  _ __ ___   ___ _ __ _ __  _ __ ___   ___ _ __| | _____ _ __ ")
print(" | . ` | | | | '_ ` _ \| '_ ` _ \ / _ \ '__| '_ \| '_ ` _ \ / _ \ '__| |/ / _ \ '__|")
print(" | |\  | |_| | | | | | | | | | | |  __/ |  | | | | | | | | |  __/ |  |   <  __/ |   ")
print(" |_| \_|\__,_|_| |_| |_|_| |_| |_|\___|_|  |_| |_|_| |_| |_|\___|_|  |_|\_\___|_|   "+reset)
print()
# ----#----#---- ABFRAGE ----#----

# ----#----#---- EINLESEN ----#----
try:
    file = open("./nummern.txt")
    inhalt = file.readlines()
except FileNotFoundError:
    print("ES WURDE DIE DATEI ZUM EINLESEN NICHT GEFUNDEN. DAS PROGRAMM BENÖTIGT 'nummern.txt' IM SELBEN VERZEICHNIS.")
    print("QUELLE ZUM HERUNTERLADEN: https://bwinf.de/fileadmin/user_upload/BwInf/2019/38/1._Runde/Material/A2/nummern.txt")
    print()
    sys.exit(0)
print(pink+"EINGABE"+reset)
for i in range(0, len(inhalt)):
    inhalt[i] = inhalt[i].strip()
print(inhalt)
print()
# ----#----#---- AUSWERTEN ----#----
print(pink+"ERGEBNIS"+reset+" (Gelb markiert sind alle Blöcke, die mit 0 anfangen.)")
anzahl = len(inhalt)
ok = 1
for u in range(0, anzahl):
    ok = 1
    nr = 0
    string = ""
    while ok:
        try:
            if inhalt[u][nr] == "0": string = string+gelb
            if inhalt[u][nr+4] != "0":
                #print("NR4 ", end=" ")
                #print(nr, len(inhalt[u])-1)
                if (len(inhalt[u])-1)-(nr+3) == 1:
                    #print(nr+3, (len(inhalt[u])-1))
                    #print("("+inhalt[u][nr+3]+")")
                    if inhalt[u][nr+2] == "0":
                        string = string+inhalt[u][nr]+inhalt[u][nr+1]+inhalt[u][nr+2]+"-"+inhalt[u][nr+3]+inhalt[u][nr+4]+reset
                    else:
                        string = string+inhalt[u][nr]+inhalt[u][nr+1]+"-"+inhalt[u][nr+2]+inhalt[u][nr+3]+inhalt[u][nr+4]+reset
                    ok = 0
                else:
                    string = string+inhalt[u][nr]+inhalt[u][nr+1]+inhalt[u][nr+2]+inhalt[u][nr+3]+reset+"-"
                    nr = nr+4
            elif inhalt[u][nr+3] != "0":
                #print("NR3 ", end=" ")
                string = string+inhalt[u][nr]+inhalt[u][nr+1]+inhalt[u][nr+2]+reset+"-"
                nr = nr+3
            elif inhalt[u][nr+2] != "0":
                #print("NR2 ", end=" ")
                string = string+inhalt[u][nr]+inhalt[u][nr+1]+reset+"-"
                nr = nr+2
            else:
                #print("ELS ", end=" ")
                if (len(inhalt[u])-1)-(nr+3) == 1:
                    if inhalt[u][nr+2] == "0":
                        string = string+inhalt[u][nr]+inhalt[u][nr+1]+inhalt[u][nr+2]+"-"+gelb+inhalt[u][nr+3]+inhalt[u][nr+4]+reset
                    else:
                        string = string+inhalt[u][nr]+inhalt[u][nr+1]+"-"+inhalt[u][nr+2]+inhalt[u][nr+3]+inhalt[u][nr+4]+reset
                    ok = 0
                else:
                    nr = nr+4
                    string = string+inhalt[u][nr-4]+inhalt[u][nr-3]+inhalt[u][nr-2]+inhalt[u][nr-1]+reset+"-"
        except IndexError:
            #print("EXC ", end=" ")
            #print((anzahl)-(anzahl-nr), len(inhalt[u])-1)
            for k in range((anzahl)-(anzahl-nr), len(inhalt[u])):
                string = string+inhalt[u][k]
            string = string+reset
            ok = 0
    # ----#----#---- ERGEBNIS ----#----
    print(string)
print()
