"""MASTER MIND"""

"""Je code ziet er goed uit, alleen sommige regels zijn iets te lang zijn volgens de PEP 8 style guide.
Je legt ook goed uit wat de speler moet doen.
Wat ik ook leuk vond om te zien is het gebruik van globale variabelen"""

import random


def begin():
    """Hier wordt de begin menu getoont waar bij de gebruiker kiest tussen de regels van het spel of het starten van
    het spel of het stoppen van het spel. """

    print("                                                    **************************************")
    print("                                                     WELKOM BIJ MATSER MIND ARE YOU READY?")
    print("                                                    **************************************\n")
    print("                                                          ========================")
    print("                                                          || 1.uitleg en regels ||")
    print("                                                          || 2.start het spel   || ")
    print("                                                          || 3.stoppen          ||")
    print("                                                          ========================\n")
    keuze = input("                                                      voer uw keuze in {1}, {2} of {3}: ")
    print("                                                 -------------------------------------------\n")

    while True:

        if keuze == "1":
            print("\ndat is fijn, hier zijn alle regels voor het spelletje: ")
            print("----------------------------------------------------------")
            regels()
            break
        elif keuze == "2":
            print("\nwat goed dat u het spelletje wil spellen,\nik hoop dat uu klaar voor bent :)")
            print("-------------------------------------------------------------------------------")
            tegenstander()
            break
        elif keuze == "3":
            print("bedankt voor het spelen :-) ")
            break
        else:
            print("FOUT probeer opnieuw: \n")
            print("========================")
            print("|| 1.uitleg en regels ||\n|| 2.start het spel   ||\n|| 3.stoppen          ||")
            print("========================")
            keuze = input("voer uw keuze in {1}, {2} of {3}: ")
            print("-------------------------------------------\n")


def regels():
    """"een functie waar bij alle game regels worden getoont """

    print(
        "\nUITLEG:\nBij Master Mind draait het allemaal om logisch nadenken, de juiste keuzes maken en concentratie.\n"
        "Het doel van het spel is om de kleurcode van de computer te achterhalen.\n"
        "De computer  is de codemaker, deze dient een code te maken met vier gekleurde pionnen.\n"
        "Deze code is alleen zichtbaar voor de computer, er kan gekozen worden uit vijf verschillende kleuren.\n")
    print(
        "REGELS:\n1. De computer zal en code maken van vier kleuren.\n2. De speler krijg 8 pogingen om de code te "
        "kraken. "
        "\n3. De speler krijgt bij elke poging een feedback."
        "\n4. Feedback bestaat uit twee pinnen {Zwart} en {Wit}."
        "\n5. Als de speler Zwart pin krijg dan heeft ie een juiste kleuer op de juiste plek."
        "\n6. Als de speler Wit pin krijg dan heeft hij een juiste kleur maar niet op de juiste plek."
        "\n7. ALs de gebruiker helemaal niks krijgt dan heeft hij helemaal niks goed.\n")
    terug = (input("Ik hoop dat u met veel plezier het spelletje speelt, succes\n"
                   "druk op {1} om het begin menu te kunnen zien : "))
    while True:
        if terug == "1":
            begin()
            break
        else:
            print("\nFOUT, u moet 1 kiezen om de begin menu te kunnen zien.\n")
            terug = (input("druk op {1} om het begin menu te kunnen zien : "))


def tegenstander():
    """een functie waar bij u tegenstander mag kiezen.


    als de gebruiker op 1 drukt dan wordt de code voor hem gemaakt en hij mag het krakken.

    en als de gebruiker op 2 drukt dan moet hij zelf de code maken voor de computer om te krakken.
        """

    print("Alright here we go, u mag kiezen uit de volgende opties: \n"
          "\n1. De computer tegen u."
          "\n2. u tegen de computer. ")
    keuze = input("Hier mag u keuze invullen 1 of 2? ")
    if keuze == "1":
        print("\nTop! dan gaat de computer een geheim code maken. ")
        start_spel_computer()
    elif keuze == "2":
        print("Top! u mag dan zo meteen de code maken voor de computer. \n")
        start_spel_gebruiker()
    else:
        begin()


def start_spel_computer():
    """Hier maakt de computer voor de gebruiker om te kunnen krakken een vervolgens wordt een feedback op gegeven met
    zwart en wit pinnen """

    global zwart_pin
    global vlag
    global code
    global kleuren
    global gok

    print(
        "de letters staan voor de hoofdletter van de kleuren.\nDus 'R' voor Rood en 'G' voor Groen en 'B' voor blauw "
        "en 'Z' voor Zwart en 'P' voor Paars en 'O' voor Oranje.")
    kleuren = ["R", "G", "B", "Z", "P", "O"]
    print(kleuren)
    code = random.sample(kleuren, 4)
    print(code)
    poging = 8
    print(f"u hebt {poging} pogingen: ")

    gok = input("kies eerste kleuren: ").upper(), input("kies tweede kleuren: ").upper(), input(
        "kies derde kleuren : ").upper(), input("kies vierde kleuren: ").upper()

    while True:
        if any(x in kleuren for x in gok):
            print(f"dat is uw gok {gok}\n")
            break
        else:
            print("\nDat is een ongeldig invoer, probeer opnieuw! ")
            print(f"hier zijn alle kleuren opnieuw {kleuren}")
            gok = input("kies eerste kleuren: ").upper(), input("kies tweede kleuren: ").upper(), input(
                "kies derde kleuren:  ").upper(), input("kies vierde kleuren: ").upper()

    feedback()
    poging = 8

    while True:
        if zwart_pin >= 4:
            print("Gefeliciteerd je hebt gewonnen!!  ")
            break

        else:
            print(
                "de letters staan voor de hoofdletter van de kleuren.\nDus 'R' voor Rood en 'G' voor Groen en 'B' "
                "voor blauw en 'Z' voor Zwart en 'P' voor Paars en 'O' voor Oranje.")
            kleuren = ["R", "G", "B", "Z", "P", "O"]
            print(kleuren)
            poging -= 1
            zwart_pin = 0
            wit_pin = 0
            print(f"u heeft {poging} pogingen: ")
            gok = input("kies eerste kleuren: ").upper(), input("kies tweede kleuren: ").upper(), input(
                "kies derde kleuren : ").upper(), input("kies vierde kleuren: ").upper()
            feedback()
        if poging < 1:
            print("U kunt helaas de code niet kraken: ")
            break


def start_spel_gebruiker():
    """Hier maakt de gebruiker de code voor de computer om te kunnen krakken een vervolgens wordt een feedback op
    gegeven met zwart en wit pinnen """

    global zwart_pin
    global wit_pin
    global code
    global kleuren
    global vlag
    global gok

    print(
        "de letters staan voor de hoofdletter van de kleuren.\nDus 'R' voor Rood en 'G' voor Groen en 'B' voor blauw "
        "en 'Z' voor Zwart en 'P' voor Paars en 'O' voor Oranje.")
    kleuren = ["R", "G", "B", "Z", "P", "O"]
    print(f"hier zijn alle kleuren {kleuren} ")
    print("\nu mag een code maken voor de computer van 4 kleuren: ")
    code = input("kies eerste kleuren: ").upper(), input("kies tweede kleuren: ").upper(), input(
        "kies derde kleuren : ").upper(), input("kies vierde kleuren: ").upper()
    gok = random.sample(kleuren, 4)

    while True:
        if any(x in kleuren for x in code):
            print(f"dat is uw code {code}\n")
            break
        else:
            print("\nDat is een ongeldig invoer, probeer opnieuw! ")
            print(f"hier zijn alle kleuren opnieuw {kleuren}")
            code = input("kies eerste kleuren: ").upper(), input("kies tweede kleuren: ").upper(), input(
                "kies derde kleuren:  ").upper(), input("kies vierde kleuren: ").upper()

    feedback()

    poging = 8
    while True:
        if zwart_pin == 4:
            print("Gefeliciteerd je hebt gewonnen!!  ")
            break

        else:
            print(
                "de letters staan voor de hoofdletter van de kleuren.\nDus 'R' voor Rood en 'G' voor Groen en 'B' "
                "voor blauw en 'Z' voor Zwart en 'P' voor Paars en 'O' voor Oranje.")
            kleuren = ["R", "G", "B", "Z", "P", "O"]
            print(kleuren)
            print(code)
            poging -= 1
            zwart_pin = 0
            wit_pin = 0
            print(f"u heeft {poging} pogingen: ")
            gok = random.sample(kleuren, 4)
            feedback()
        if poging < 1:
            print("U kunt helaas de code niet kraken: ")
            break


def feedback():
    """deze functie laat de feedback zien op de gok die de computer of de gebruiker maakt."""

    global code
    global gok
    global kleuren
    global zwart_pin
    global wit_pin
    global vlag

    vlag = [1, 1, 1, 1]
    zwart_pin = 0
    wit_pin = 0

    for i in range(0, len(code)):
        if gok[i] == code[i]:
            vlag[i] = 0
            zwart_pin += 1

    print(f"Uw feedback is {zwart_pin} zwart pin,en dat is uw gok {gok}")

    for i in range(0, len(code)):
        if vlag[i] == 1:
            for x in range(0, len(code)):
                if gok[i] == code[x] and vlag[x] == 1:
                    vlag[x] = 0
                    wit_pin += 1

    print(f"Uw feedback is {wit_pin} wit pin,en dat is uw gok {gok}\n")


def alle_oplossingen():
    """Hier worden alle mogelijk optie getoont die de computer moet gebruiken om de code te kunnen krakken"""

    kluerens = "RGBZPO"
    oplossingen = []
    for i in range(len(kluerens)):
        for x in range(len(kluerens)):
            for y in range(len(kluerens)):
                for z in range(len(kluerens)):
                    mogelijk_oplossing = kluerens[i] + kluerens[x] + kluerens[y] + kluerens[z]
                    oplossingen.append(mogelijk_oplossing)
    return print(oplossingen)


# alle_oplossingen()
# start_spel_gebruiker()
begin()
# print(start_spel())
