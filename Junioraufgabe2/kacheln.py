# -*- coding: utf8 -*-
#!/usr/bin/env python3
# python3.7.0
# (c) Snocember, 2019
# BWINF 2019, Aufgabe Kacheln

# ----#---- Importe, Initialisierungen und Definitionen ----#----
import sys
# ascii-farben
rst = "\033[0m"
bl  = "\033[104m"
grn = "\033[42m"
wss = "\033[30;107m"
cyn = "\033[96m"
red = "\033[101m"
glb = "\033[30;103m"
newbl = "\033[95;106m"
newgrn= "\033[95;102m"

print("Das Programm erfordert für ein angenehmes Bedienen eine Terminal-Umgebung mit ANSI-Farbunterstützung.")
print(cyn)
print(" _  __          _          _       ")
print("| |/ /__ _  ___| |__   ___| |_ __  ")
print("| ' // _` |/ __| '_ \ / _ \ | '_ \ ")
print("| . \ (_| | (__| | | |  __/ | | | |")
print("|_|\_\__,_|\___|_| |_|\___|_|_| |_|")
print(rst)

xdim = 0
ydim = 0
karte = []
kacheln = []
kachelreihe = []
Fkacheln = [] #für Farben
Fkachelreihe = [] #für Farben
cKacheln = [] #später geclonte kacheln-liste
#xmsg = True

def check(parY,parX,y,x,d):
    sf = 0 #Sternfaktor sf
    nf = 0 #NullFaktor nf
    ef = 0 #EinsFaktor ef
    nummer = 0
    if parY == -1 or parY == 0:
        nummer = nummer+1
        if (y-1)%2:
            if ckacheln[y-1][x] == "0": nf = nf+1
            elif ckacheln[y-1][x] == "1": ef = ef+1
            elif ckacheln[y-1][x] == "*": sf = sf+1
        else:
            sf = sf+1

    if parY == 1 or parY == 0:
        nummer = nummer+1
        if (y)%2:
            if ckacheln[y+1][x] == "0": nf = nf+1
            elif ckacheln[y+1][x] == "1": ef = ef+1
            elif ckacheln[y+1][x] == "*": sf = sf+1
        else:
            sf = sf+1

    if parX == -1 or parX == 0:
        nummer = nummer+1
        if (x-1)%2:
            if ckacheln[y][x-1] == "0": nf = nf+1
            elif ckacheln[y][x-1] == "1": ef = ef+1
            elif ckacheln[y][x-1] == "*": sf = sf+1
        else:
            sf = sf+1

    if parX == 1 or parX == 0:
        nummer = nummer+1
        if (x)%2:
            if ckacheln[y][x+1] == "0": nf = nf+1
            elif ckacheln[y][x+1] == "1": ef = ef+1
            elif ckacheln[y][x+1] == "*": sf = sf+1
        else:
            sf = sf+1
    #---
    #print("----------- ("+str(nummer)+") -> "+str(sf)
    if d == 3:
        return "0"
    if nummer == 2:
        if sf==2:
            return "*"
    elif nummer == 3:
        if sf==3:
            return "*"
    elif nummer == 4:
        if sf==4:
            return "*"
    if nf == 0 and ef>nf:
        return "1"
    elif ef == 0 and nf>ef:
        return "0"
    elif nf == 0 and ef == 0:
        return "*"
    else:
        return "x"


# ----#----#---- ABFRAGE ----#----

print("Verfügbare Karten: 0, 1, 2, 3, 4, 5, 6")
print("_ _ _ _ _ _ _ _ _ (6 ist eine eigene karte)")
input = input("Ausgewählte Karte-nr: ")
try:
    if input != "0":
        if input != "1":
            if input != "2":
                if input != "3":
                    if input != "4":
                        if input != "5":
                            if input != "6":
                                print()
                                print("ES DARF IN DAS INPUT-FELD NUR EINE ZAHL VON 0 BIS 6 EINGEGEBEN WERDEN.")
                                print()
                                sys.exit(0)
    if input == "0":
        file = open("./map_spacy.txt")
    else:
        file = open("./map"+input+"_spacy.txt")
    content = file.read()
except FileNotFoundError:
    print()
    print("ES WURDE DIE DATEI ZUM EINLESEN NICHT GEFUNDEN. DAS PROGRAMM BENÖTIGT 'map"+input+"_spacy.txt' IM SELBEN VERZEICHNIS.")
    print("QUELLE ZUM HERUNTERLADEN: https://bwinf.de/fileadmin/user_upload/BwInf/2019/38/1._Runde/Material/J2/map"+input+"_spacy.txt")
    print()
    sys.exit(0)

# ----#----#---- EINLESEN ----#----
#content = urllib.urlopen(url1).read()
#print("Eingelesene Daten:"
#print(content)

karte = content.split()
ydim = int(karte[0])
xdim = int(karte[1])
karte.pop(0)
karte.pop(0)
print("dimensionen: x"+str(xdim)+"y"+str(ydim))
#print("ursprüngl. karte: "+str(karte))

for y in range(0, ydim*2):
    kachelreihe = []
    Fkachelreihe = []
    for x in range(0, xdim*2):
        kachelreihe.append(karte[0])
        if karte[0] == "0": Fkachelreihe.append(bl+karte[0]+rst)
        if karte[0] == "1": Fkachelreihe.append(grn+karte[0]+rst)
        if karte[0] == "*": Fkachelreihe.append(wss+karte[0]+rst)
        #print karte[0]
        karte.pop(0)
        #print("veränderte karte: "+str(karte))
    kacheln.append(kachelreihe)
    Fkacheln.append(Fkachelreihe)
ckacheln = kacheln # Kacheln werden geclont

# ----#----#---- anschaulichere Farb-vor-ausgabe ----#----
anzahl1 = len(Fkacheln)
anzahl2 = len(Fkachelreihe)
print(red+"KARTE"+rst+":")
for k in range(0, anzahl1):
    for i in range(0, anzahl2):
        print(Fkacheln[k][i], end="")
        if i % 2: print("", end=" ")
    print()
    if k % 2: print()

# ----#----#---- AUSWERTEN----#----
#schleife = 1
#while schleife==1:
for d in range(0,10):
    #print("##### ----- ##### ----- NEUE RUNDE")
    us = 0 #übrige sternfelder
    for y in range(0, ydim*2):
        for x in range(0, xdim*2):
            #xmsg = True
            if kacheln[y][x] == "*": #checkt ob das feld * ist
                us = us+1
                #print("kacheln["+str(y)+"]["+str(x)+"]"+" =", end=" ")
                if y == 0: # checkt ob das feld in der ersten reihe ist
                    #print("/\\", end="")
                    if x == 0: #checkt ob das feld bei 0,0 sich befindet
                        #print("< --> wasser")
                        ckacheln[y][x] = "0"
                        Fkacheln[y][x] = newbl+"0"+rst
                    elif x == anzahl2-1: # checkt ob das feld am rechten ende der reihe ist
                        #print("> --> wasser")
                        ckacheln[y][x] = "0"
                        Fkacheln[y][x] = newbl+"0"+rst
                    else:
                        #print(".")
                        check1 = check(1,0,y,x,d)
                        if check1 == "0":
                            ckacheln[y][x] = "0"
                            Fkacheln[y][x] = newbl+"0"+rst
                        elif check1 == "1":
                            ckacheln[y][x] = "1"
                            Fkacheln[y][x] = newgrn+"1"+rst
                        elif check1 == "x":
                            ckacheln[y][x] = "x"
                            Fkacheln[y][x] = red+"x"+rst
                elif y == anzahl1-1: # checkt ob das feld in der untersten reihe ist
                    #print("\\/", end="")
                    if x == 0: # checkt ob das feld an der Nullstelle in der untersten Reihe ist
                        #print("< --> wasser")
                        ckacheln[y][x] = "0"
                        Fkacheln[y][x] = newbl+"0"+rst
                    elif x == anzahl2-1:
                        #print("> --> wasser")
                        ckacheln[y][x] = "0"
                        Fkacheln[y][x] = newbl+"0"+rst
                    else:
                        #print(".")
                        check1 = check(-1,0,y,x,d)
                        if check1 == "0":
                            ckacheln[y][x] = "0"
                            Fkacheln[y][x] = newbl+"0"+rst
                        elif check1 == "1":
                            ckacheln[y][x] = "1"
                            Fkacheln[y][x] = newgrn+"1"+rst
                        elif check1 == "x":
                            ckacheln[y][x] = "x"
                            Fkacheln[y][x] = red+"x"+rst
                else: # alle anderen möglichkeiten:
                    #print(".", end="")
                    if x == 0: # checkt ob das feld am linken Rand ist
                        #print("<")
                        check1 = check(0,1,y,x,d)
                        if check1 == "0":
                            ckacheln[y][x] = "0"
                            Fkacheln[y][x] = newbl+"0"+rst
                        elif check1 == "1":
                            ckacheln[y][x] = "1"
                            Fkacheln[y][x] = newgrn+"1"+rst
                        elif check1 == "x":
                            ckacheln[y][x] = "x"
                            Fkacheln[y][x] = red+"x"+rst
                    elif x == anzahl2-1: # checkt ob das feld am rechten Rand ist
                        #print(">")
                        check1 = check(0,-1,y,x,d)
                        if check1 == "0":
                            ckacheln[y][x] = "0"
                            Fkacheln[y][x] = newbl+"0"+rst
                        elif check1 == "1":
                            ckacheln[y][x] = "1"
                            Fkacheln[y][x] = newgrn+"1"+rst
                        elif check1 == "x":
                            ckacheln[y][x] = "x"
                            Fkacheln[y][x] = red+"x"+rst
                    else: # alle Felder in der Mitte:
                        #print(".")
                        check1 = check(0,0,y,x,d)
                        if check1 == "0":
                            ckacheln[y][x] = "0"
                            Fkacheln[y][x] = newbl+"0"+rst
                        elif check1 == "1":
                            ckacheln[y][x] = "1"
                            Fkacheln[y][x] = newgrn+"1"+rst
                        elif check1 == "x":
                            ckacheln[y][x] = "x"
                            Fkacheln[y][x] = red+"x"+rst

print()
# ----#----#---- ERGEBNIS ----#----

print("\033[96m"+"-----------------------------------"+rst)
print(red+"ERGEBNIS"+rst+": ("+bl+"altes Wasser,"+grn+" altes Land,"+newbl+" neu gen. Wasser,"+newgrn+" neu gen. Land"+rst+")")
for k in range(0, anzahl1):
    for i in range(0, anzahl2):
        print(Fkacheln[k][i], end="")
        if i % 2: print(" ", end="")
    print()
    if k % 2: print()
print("\033[96m"+"-----------------------------------"+rst)
for k in range(0, anzahl1):
    for i in range(0, anzahl2):
        print(ckacheln[k][i], end="")
        if i % 2: print(" ", end="")
    print()
    if k % 2: print()
print("\033[96m"+"-----------------------------------"+rst)
