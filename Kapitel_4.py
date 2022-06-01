from Bibliothek import question, abfrage
from Kapitel_3 import Inventar

# Abfrage
def loop():
    print("Um zur Bibliothek zurück zu gehen enter 'Bibliothek' oder 'l'.\n")
    print("Um das Spiel zu beenden enter 'quit'.\n")
    # S3
    k4abfrage()

def k4abfrage():
    i = input()
    if i == "Bibliothek" or i == "l":
        abfrage()
    elif i == "quit":
        print("\n\n\n\n\n\n\n\nDanke für eure Aufmerksamkeit")
        # S3
    else:
        "Error. Please try again"
        # S3



## Aktionen

# pa25
def pa25():
    a2 = input()
    if a2 == "1" or a2 == "Therme":
        pa21()
    elif a1 == "2" or a1 == "Amphietheater":
        print("Beim Amphietheater angekommen, läuft Servius gut gelaunt auf eine Gruppe von Menschen zu.\n")
        print(
            "Er stellt dir nach kurzem Begrüßen, alle vor: Julia lächelt dich an. Gaius und Quintus wirken auch ganz nett.\n")
        print("Gemeinsam schlendert ihr um das große Gebäude herum, lachend und plaudernd.\n")
        print("Vielleicht hast du schon Freunde im alten Rom gefunden?")
        p3()


# pa24
def pa24():
    a3 = input()
    if a3 == "1" or a3 == "Einstecken":
        print("\nDu packst den Apfel in deinen Beutel. Da der Besitzer es allerdings bemerkte, \ngibt er Servius für trotz Geld keinen weiteren Apfel.\n")
        print("Dieser ist etwas wütend auf dich, vergibt dir aber nach einer Entschuldigung. \nIhr teilt euch den gestohlenen Apfel.\n")
        p3()
    elif a3 == "2" or a3 == "Aufheben":
        print("Du legst den Apfel höflich zurück.\n")
        print("Als Dank schenkt dir der Besitzer 2 Äpfel, die du froh einsteckst.\n")
        Inventar.append("2 Äpfel")
        print("Ihr esst die 2 bezahlen gemütlich auf einer Steinmauer und plaudert ein wenig.\n")
        p3()
    else:
        print("\nError.Please try again.\n")
        # S3
        pa24()

# pa23
def pa23():
    a3 = input()
    if a3 == "1" or a3 == "ja":
        pa22()
    elif a3 == "2" or a3 == "nein":
        print("Er kauft einen Apfel, den ihr schließlich teilt, da du doch Lust hattest.\n")
        p3()
    else:
        print("\nError. Please try again.\n")
        # S3
        pa23()

# pa22
def pa22():
    print("Servius geht hin und bezahlt die Äpfel.\n")
    print("Du siehst wie einer hinunterfällt, doch die anderen scheinen es nicht zu bemerken.")
    print("Was machst du?\n")
    # S3
    print("1 heimlich Einstecken\n")
    print("2 Aufheben\n")
    # S3
    pa24()



# pa21
def pa21():
    print("Wir gingen Richtung Therme. Leider hatte diese jedoch geschlossen.\n")
    print("Als wir gerade wieder gehen wollten, weiste mich Servius auf einen Obstverkäufe hin.")
    print("Er fragte mich ob ich auch einen Apfel haben möchtest.")
    print("Was machst du?\n")
    # S3
    print("1 ja\n")
    print("2 nein\n")
    # S3
    pa23()




## Storyline

# para 3
def p3():
    print("\nmaintenance error\n")
    print("Geschichte muss erst fortgesetzt werden.\n")
    print("Um zur Bibliothek zurück zu gehen enter 'Bibliothek' oder 'l'.\n")
    print("Um das Spiel zu beenden enter 'quit'.\n")
    # S3
    k4abfrage()


# para 2
def p2():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("'Aha, danke.'")
        if question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("'Bitte. Würdest du jetzt lieber zur Therme oder zum Amphietheater gehen?'")
            print("Was machst du?\n")
            # S3
            print("1 Therme\n")
            print("2 Amphietheater\n")
            # S3
            pa25()


# para 1
def p1():
    print("\n\n_______________________________________\n")
    print("\nKapitel 4")
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("Am nächsten Morgen war ich immer noch verwirrt.\n")
        print("Mittlerweile hatte ich verstanden, dass ich im alten Rom war. Da stellte sich mir nur eine Frage: 'Wie bin ich hierhergekommen?'\n")
        if  question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("Da ich vom Rumsitzen keine Antworten auf meine Fragen bekam, baschloss ich das Angebot einer Führung durch Rom von Servius anzunehmen.\n")
            print("Zum Frühstück gab es trockenes Brot und dann ging es auch schon los... \nViel zu früh aber naja in Rom beginnt der Alltag früh.\n")
            print("Natürlich gingen wir alles zu Fuß.\n")
            if question("\n-Press Enter-\n", [""]) == "":
                print("'Rechts [potes videre] das Forum.'\n ")
                # S4
                print("Ich muss mich immer noch an dieses Latein-Deucht gewöhnen.\n Eine neue Sprache: Latsch.\n")
                #help wie soll ich das formulieren
                l1 = input("Übersetze\n")
                if l1 == "kannst sehen" or l1 == "sehen kannst":
                    print("\nrichtig\n")
                    # S3
                    p2()
                else:
                    print("\nLösung: kannst sehen (2.P., Sg., Präsens)\n")
                    # S3
                    p2()

# start
p1()