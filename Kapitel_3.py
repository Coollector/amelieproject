

## to-do list
# p4a1 Funfact über Münzen
# eventuell '' und "" tauschen?


## Legende

# S1 = Roboter/Wissen
# S2 = Gedanken
# S3 = Spielanweisungen
# S4 = Latein-Deutsch Übersetzung

# g_ = Gedankenvariable
# l_ = Lateinveriable
# p_ = Paragraph
# _a_ = Aktion
# _m_ = Karte
# _u_ = Umgebung
# _i_ = Inventaraktionen
# i_= inputvariable


## Aktionen

# importe
from Bibliothek import question, name, biblituto
from Kapitel_2 import Inventar


# p4i
def p4i():
    ia = input()
    if ia == "Inventar" or ia == "e":
        print(Inventar)
        ia = input()
        if ia == "use 0" or ia == "use Münzen":
            print(Inventar[0] + " nicht verwendbar\n")
        else:
            print("Inventar geschlossen\n")
        p5()



# actions
# p4a
def p4a():
    print("\n- Enter '1', '2' oder '3' oder das dazugehörige Verb im Infinitiv -\n")
    i = input()
    if i == "1" or i == "Inspezieren":
        l4a1()
    elif i == "2" or i == "Einstecken":
        p4a2()
    elif i == "3" or i == "Ignorieren":
        p5()
    else:
        print("Error, PLease try again")
        # S3
        p4a()


def l4a1():
    print("\nMaintenance Error. Information nicht enthalten. Spiele weiter.\n")
    p5()

def p4a2():
    print("Du hast die Münzen eingesteckt.\n")
    Inventar.append("Münzen")
    print("     Enter 'Inventar' oder 'e' um dein Inventar zu öffnen\n")
    p5()



# Umgebungen
# p1u
def p1u():
    print("\nDu liegst in einem Bett.\nRechts neben dem Bett liegt Gewand auf einer Stufe in der Wand.\nLinks an der Wand gegenüber von dir ist ein Durchgang.\nDer Durchgang ist mit einem Vorhang geschlossen, doch Licht scheint durch.\n")
    # S3
    if question("\n-Press Enter-", [""]) == "":
        # S3
        p3()


# Karten
# p3m
def p3m():
    print("insert according map\n")
    if question("\n-Press Enter-", [""]) == "":
        # S3
        p4()


## storyline

# para 11
def p11():
    if question("", [""]) == "":
        # S3
        print("Oh ok...\n")
        biblituto()





# para 10
def p10():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("'Er ist ein Gelehrter, aber nun ja... er hat tendeziell eher unbeliebte Meinungen.'\n")
        if question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("'Oh ok...'\n")
            if question("\n-Press Enter-\n", [""]) == "":
                # S3
                print("'Komm ich zeig dir unsere Bücherei. Das dir [placebis]!'\n")
                # S4
                print("- Übersetze -\n")
                if input() == "wird gefallen":
                    print("\nrichtig")
                    # S3
                    p11()
                else:
                    print("\nFalsch! Lösung: wird gefallen (2.P., Sg., Futur 1, placere)")
                    # S3
                    p11()



# para 9
def p9():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("'Egal...'\n")
        if question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("'Für jetzt kannst du bei uns bleiben. Das da hinten ist mein Vater.'\n")
            if question("\n-Press Enter-\n", [""]) == "":
                # S3
                print("'[Er(= Is) ist dein Vater?]'\n")
                # S4
                print("- Enter den ganzen Satz in [] mit Satzzeichen und Groß-Klein-Schreibung -\n")
                # S3
                l = input()
                if l == "Is tuus pater est?" or l =="Is pater tuus est?":
                    print("\nrichtig\n")
                    # S3
                    p10()
                else:
                    print("\nLösung: Is tuus pater est?\n")
                    # S3
                    p10()


# para 8
def p8():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("'Ich bin " + name + ".'\n")
        if question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("'So viel wusste ich schon, aber was machst du hier?'\n")
            if question("\n-Press Enter-\n", [""]) == "":
                # S3
                print("'Ich [weiß] es [nicht].'\n")
                print("- Übersetze -\n")
                if input() == "non scio":
                    print("\nrichtig\n")
                    # S3
                    p9()
                else:
                    print("\nLösung: non scio (1.P., Sg., Präsens, Verneinung)\n")
                    p9()


# para 7
def p7():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("Der junge Mann deutete mir, mich zu setzen und etwas von dem gedeckten Tisch zu essen. \nIch verstand nicht ganz wo ich plötzlich gelandet war, doch mir schien ich kann diesem... Servius vertrauen.\n")
        if question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("Nach einer Weile stillem Essen, schaute Servius mich neugierig an.\n")
            if question("\n-Press Enter-\n", [""]) == "":
                # S3
                print("'Willst du mir [erzählen], wer du bist?'\n")
                print("- Übersetze -\n")
                if input() == "narras":
                    print("\nrichtig\n")
                    p8()
                else:
                    print("\nFalsch! Lösung, narras (2.P., Sg., Präsens, narrare)\n")
                    p8()


# para 6
def p6():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("'Was?'\n")
        if question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("'[Quid est?]'\n")
            # S4
            print("- Übersetze den Satz innerhalb der Klammer [] mit Satzzeichen und Groß-Klein-Schreibung -\n")
            # S3
            l = input()
            if l == "Was ist?" or l == "Was?":
                print("\nrichtig\n")
                p7()
            else:
                print("\nLösung: Was ist?\n")
                p7()



# para 5
def p5():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("Als ich noch einmal um die Ecke ging, sah ich den Typ von vorher, Servitus oder so.\n")
        if question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("'Du bist doch wieder aufgewacht!'\n")
            if question("\n-Press Enter-\n", [""]) == "":
                # S3
                print("'ja...'\n")
                if question("\n-Press Enter-\n", [""]) == "":
                    # S3
                    print("'Wie geht's dir? Du einen ganzen tag [dormivisti]!'\n")
                    print("- Enter die deutsche Übersetzung von den [] in richtiger Zeit, Zahl, Person OHNE Personalpronomen -\n")
                    # S3
                    i = input()
                    if i == "schliefst" or i == "hast geschlafen":
                        print("\nrichtig\n")
                        p6()
                    else:
                        print("\nLösung: schliefst (2.P., Sg., Perfekt, dormire)\n")
                        p6()


# para 4
def p4():
    print("Im Gang lagen einige Münzen auf einer Kommode.\n")

    print("\n1 Inspeziere die Münzen\n")
    print("2 Stecke die Münzen ein\n")
    print("3 Ignoriere die Münzen")
    # S1
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("Ich hatte mir eigentlich nichts zu den Münzen gedacht, doch in meinem Kopf erschienen diese Optionen...\n")
        if question("\n-Press Enter-", [""]) == "":
            # S3
            p4a()


# para 3
def p3():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("Ich hörte Stimmen in der Nähe. \nAls ich durch den Vorhang und um die Ecke ging, hatte ich das Gefühl als würde in meinem Kopf eine Karte gezeichnet werden von jedem Ort an dem ich mich aufhielt.\n")
        print("- Enter 'Standort' oder 'k' für deine Karte -\n")
        # S3
        i = input()
        if i == "Standort" or i == "k":
            p3m()
        else:
            p4()


# para 2
def p2():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("Ich wusste genau was um mich herum geschah... selbst, wenn ich mich gar nicht darauf konzentrierte.\n")
        print("- Enter 'Umgebung' oder 's' für eine Beschreibung deiner Umgebung (falls möglich) -\n")
        # S3
        i = input()
        if i == "Umgebung" or i == "s":
            p1u()
        else:
            p3()


# para 1
def p1():
    print("\n\n_______________________________________\n")
    print("\nKapitel 3")
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("\nAls ich meine Augen öffnete, fühlte sich alles surreal an. Es war ein seltsam starkes Gefühl der Selbstkontrolle.\n")
        if question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("Du liegst in einem Bett.\nRechts neben dem Bett liegt Gewand auf einer Stufe in der Wand.\nLinks an der Wand gegenüber von dir ist ein Durchgang.\nDer Durchgang ist mit einem Vorhang geschlossen, doch Licht scheint durch.\n")
        # S1
        p2()


# start
p1()