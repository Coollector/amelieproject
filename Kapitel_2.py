

### Kapitel 2

## import
from Bibliothek import question
from Bibliothek import Inventar

# Kapitel 3
def k3():
    import Kapitel_3


## Aktionen

# pa2
def pa2():
    i = input()
    if i == "1":
        print("\nDu steckst das Feuerzeug in deine rechte Hosentasche. Merke dir, dass du es besitzt.")
        Inventar.append("Feuerzeug")
        p2()
    elif i == "2":
        print("\nDu machst einige schnelle Schritte um die anderen aufzuholen.\n")
        p2()
    else:
        print("\nError. Please try again.\n")
        # S3
        pa2()

# pa1
def pa1():
    i = input()
    if i == "1" or i == "Weitergehen":
        print("\nDu gehst weiter.\n")
        p2()
    elif i == "2" or i == "Stehenbleiben":
        print("\nDu bückst dich und bindest deinen Schuh neu. In der Zwischnezeit haben dich alle überholt.")
        print("\nAls du gerade wieder aufstehen willst, siehst du ein Feuerzeug am Boden liegen.\nWas tust du? (1 oder 2)\n")
        print("\n1 Mitnehmen\n")
        print("2 Weitergehen\n")
        p2a()
    else:
        print("\nError. Please try again.\n")
        # S3
        pa1()



## Storyline

# para 2
def p2():
    print("Geimeinsam mit den anderen, betrittst du einen größeren Kellerraum.\n")
    if question("\n-Press Enter-\n", [""]) == "":
        print("Du siehst dich um: Die Decke ist relativ hoch, in der Mitte des Raumes steht ein Altar.\n")
        print("Du gehst auf den Altar zu, da deine Lehrerin alle näher ruft. Sie lehnt sich - wie sie es oft tut, gegen den Altar.\n")
        if question("\n-Press Enter-\n", [""]) == "":
            print("Da geht auf einmal eine Art Portal auf. Grelles Licht blendet dich, und du willst deinen Blick abwenden.")
            print("Doch plötzlich siehst du wie jemande deine Lehrerin packt und durchs Portal zieht. Einige Mitschlüler fallen auch hinein.")
            print("Andere, so scheint es, werden förmlich ins Protal gezogen.\n")
            if question("\n-Press Enter-\n", [""]) == "":
                print("Instinkiv willst du wegrennen, aber es ist zu spät.\n Du spürtst den Sog, Wind in deinen Haaren und Schmerz in deinen Knochen.\n")
                print("Dann wird alles um dich herum schwarz.\n")
                k3()

# para 1
def p1():
    print("\n\n_______________________________________\n")
    print("\nKapitel 2")
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("Die Klassenfahrt nach Rom war einer der entscheidenden Gründe Latein weiter zu wählen.\nWir hatten uns alle schon unglaublich darauf gefreut.\n")
        if question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("Die Zugfahrt, war schon ein Ereignis an sich und der erste Tag auch sehr lustig.")
            print("Am Zweiten beschloss unsere Latein Professorin, zur Unzufriedenheit aller, mit uns einen alten Tempel zu besichtigen.\n")
            if question("\n-Press Enter-\n", [""]) == "":
                # S3
                print("Die Führung hätte nicht langweiliger sein können.\nDer alte Mann schlief selbst fast ein, als er uns über den Bau erzählte.\nEs war sogar schlimmer als Doppelstunde Deutsch und Koso hintereinander.")
                print("Niemand passte genau auf und um ehrlich zu sein, hörte nicht einmal ich ihm zu – was ich später noch bereuen würde.")
                print("Der letzter Stopp dieser Führung war der Keller, so alt ,dass er noch original erhalten war.... \n")
                if question("\n-Press Enter-\n", [""]) == "":
                    # S3
                    print("Um dich herum ist es finster. Eng aneinander gedrängt geht ihr den schmalen Gang entlang.\n")
                    print("Da bemerkst du, dass dein Schnürsenkel offen ist.\nWas tust du? (1 oder 2)\n")
                    print("\n1. Ich gehe weiter...Ich habe doch keine Lust alleine zurückzufallen. -> Antwort: 1\n")
                    print("2. Ich bleibe stehen und binde natürlich meinen Schuh neu. -> Antwort: 2\n")
                    pa1()



# start
p1()

