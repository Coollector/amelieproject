
###Kapitel 1

## importe
from Bibliothek import question, name

## storyline

# para 5
def p5():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("Der Soldat stütze mich und ging mit mir aus der schmalen Gasse heraus.\n")
        print("Er hatte Recht gehabt; es war ein schwerer begehbarer Weg durch dichtes Gestrüpp.\n")
        print("Was macht er dann hier?\n")
        if question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("Verloren in Gedanken merkte ich nicht wie wir noch einmal um die Ecke gingen.\n Wir standen plötzlich vor einer riesigen Menschenmenge.\n")
            print("Vor dem Tempel war großer Tumult. ")
            print("Jeder versuchte hineinzukommen, doch die Mönche gestatteten nur einzelnen den Eintritt. Natürlich erst nach Bezahlung.\n")
            print("Ich blickte nur kurz über das Geschehen der Menschen, als ich plötzlich inmitten der Masse ein mir bekannt erscheinendes Gesicht sah.\n")
            if question("\n-Press Enter-\n", [""]) == "":
                # S3
                print("Ihre Augen starrten mich an, trafen meine nur kurz und schauten sofort wieder weg.\n")
                print("Sie flüsterte nur, so leise, dass ich es mir auch nur hätten einbilden können, doch es tat in meinen Ohren weh: 'Invenis me!'\n")
                if question("\n-Press Enter-\n", [""]) == "":
                    # S3
                    import Kapitel_2


# para 4
def p4():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("'Non [scire].'\n")
        # S4
        print("Setze in die richtige Form (1.P. Sg. Präsens\n")
        # S3
        if input() == "scio":
            print("\nrichtig\n")
            # S3
            p5()
        else:
            print("\nLösung: scio (1.P., Sg., Präsens, scire 4)\n")
            # S3
            p5()


# para 3
def p3():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("Was war das? – Einfach mal mitspielen, vielleicht erfahr ich dann mehr.\n")
        if question("\n-Press Enter-\n", [""]) == "":
            # S3
            print("'Komm mit.'\n")
            if question("\n-Press Enter-\n", [""]) == "":
                # S3
                print("'Du sprichst Deutsch!?'\n")
                if question("\n-Press Enter-\n", [""]) == "":
                    # S3
                    print("'Was? Deutsch? Nein, ich spreche Latein ...'\n")
                    if question("\n-Press Enter-\n", [""]) == "":
                        # S3
                        print("'Latein?? Ich spreche kein Latein und du -'\n")
                        if question("\n-Press Enter-\n", [""]) == "":
                            # S3
                            print("'Egal. Schaffen wir dich hier weg. - Wie bist du überhaupt hier gelandet? Hinter den Tempel kommt man allein nicht so einfach hin. \nVor allem nicht in deinem Zustand. Wie viel du [bibisti]?'\n")
                            # S4
                            print("- Übersetze -\n")
                            # S3
                            l2 = input()
                            if l2 == "hast getrunken" or l2 == "trankst":
                                print("\nrichtig\n")
                                # S3
                                p4()
                            else:
                                print("\nFalsch! Lösung: hast getrunken (2.P., Sg., Perfekt, bibere 3)\n")
                                p4()


# para 2
def p2():
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("'Ego (esse) " + name + ".'")
        l1 = input("\n- Enter die richtige Form von esse -\n")
        # S3
        if l1 == "sum":
            print("\nrichtig")
            # S3
            p3()
        else:
            print("\nFalsch! Lösung: sum (1.P, Sg., Präsens, esse)")
            # S3
            p3()


# para 1
def p1():
    print("\n\n_______________________________________\n")
    print("Kapitel 1\n")
    if question("\n-Press Enter-\n", [""]) == "":
        # S3
        print("'Hey! Hey! Wach auf! Was machst du hier?!'\n")
        print("Was war das für eine Stimme? Warum tut mein Kopf so weh? Was ist los?\n")
        # S2
        print("Ich wollte die Augen öffnen, aber irgendwie fühlte sich mein Augenlied unendlich schwer an.\n")
        if question("\n-press enter-", [""]) == "":
            # S3
            print("Jemand berührte meine Schulter, rüttelte mich.\n")
            if question("\n-Press Enter-\n", [""]) == "":
                # S3
                print("'Hey! Was ist los mit dir? Wach auf, sonst muss ich jemanden holen.'\n")
                print("Ich öffnete meine Augen. Licht. So viel Licht.\n")
                print("Als ich endlich etwas erkennen konnte, sah ich eine Silhouette über mich gebeugt.\n")
                print("Breite Schultern, starke Arme in einer . . . Soldatenuniform? Antike, römische Soldatenbekleidung?? Wo bin ich hier?\n")
                if question("\n-Press Enter-\n", [""]) == "":
                    # S3
                    print("'Schau nicht so entgeistert. Cur ibi es?'\n")
                    # S4
                    print("'Was?'\n")
                    print("'Quid est?'\n")
                    # S4
                    if question("\n-Press Enter-\n", [""]) == "":
                        # S3
                        print("'Hä soll das ein Witz sein? Wer bist du? –- Wo ist die Kamera?'\n")
                        if question("\n-Press Enter-\n", [""]) == "":
                            # S3
                            print("'Ich Servius sum.'\n")
                            # S4
                            print("'Was?'\n")
                            print("'Quid est?'\n")
                            # S4
                            p2()

# start
p1()