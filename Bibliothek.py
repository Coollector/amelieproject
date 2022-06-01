
## to-do list
# p4a1 Funfact über Münzen
# eventuell '' und "" tauschen?
# kapitelspeicherung

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



### Bibliothek

Inventar = []


## Abfrage

def help():
    print("Um zur Kapitel-Übersicht zu kommen gib 'Übersicht' oder 'b' ein.\n")
    print("Um zum nächsten Kapitel zu kommen gib 'quick start' oder 'n' ein.\n")
    print("Um zur Inventar Übersicht zu kommen gib 'Inventar' oder 'e' ein.\n")
    print("Um das Spiel zu verlassen gib 'quit game' ein.\n")
    abfrage()

def nextchapter():
    import Kapitel_4

def übersicht():
    print("Um bei dem nächsten Kapitel zu starten gib 'quick start' oder 'n' ein.\n")
    abfrage()


def abfrage():
    # Inventar
        print("~Bibliothek~")
        i = input()
        if i == "Inventar" or i == "e":
            if Inventar == []:
                print("Inventar empty")
                abfrage()
            else:
                print(Inventar)
                abfrage()
        elif i == "quick start" or i == "n":
            nextchapter()
        elif i == "Übersicht" or i == "b":
            übersicht()
        elif i == "quit game":
            print("\n\n\n\n\n\n\n\nDanke für eure Aufmerksamkeit")
        elif i == "help":
            help()
        else:
            print("Error.Please try again.\n")
            # S3
            abfrage()




## questions

def question(text, stringArray):
    while True:
        antwort = input(text).strip()
        if antwort in stringArray:
            break
    return antwort




## namegiving
name = input('enter your name:\n')


## start game

def start():
    q1 = "Do you want to start the game?\n"
    q2 = "Do you want to quit the game?\n"
    a1 = input(q1)
    if a1 == "yes":
        # Kapitel_2
        a = ""
    elif a1 == "no":
        a2 = input(q2)
        if a2 == "yes":
            print("quit")
        elif a2 == "no":
            while a2 == "no" or not a1 == "yes":
                a1 = input(q1)
                if a1 == "yes":
                    # Kapitel_2
                    break
                elif a1 == "no":
                    a2 = input(q2)
                    if a2 == "yes":
                        print("quit")
                        break
        else:
            print("Invalid answer, please try again")
            start()
    else:
        print("Invalid answer, please try again")
        start()



## Tutorial

def biblituto():
    print("\n\n_______________________________________\n")
    print(" ~Willkommen in der Bibliothek~\n")
    print("Dies ist die Lobby des Spieles. Hier startest und beendest du deine Kapitel.\n")
    print("Für deine Eingabemöglichkeiten gib 'help' ein.\n")
    abfrage()

# start
