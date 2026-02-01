import hashlib
import os
import time
from datetime import datetime
from getpass import getpass


def clear():
    os.system("clear")


def loading(text="Lade", dauer=1):
    print(text, end="", flush=True)
    for _ in range(3):
        time.sleep(dauer / 3)
        print(".", end="", flush=True)
    print()


def hash_passwort(passwort):
    return hashlib.sha256(passwort.encode()).hexdigest()


def passwort_erstellen():
    clear()
    print("Passwort erstellen\n")
    while True:
        pw1 = getpass("Neues Passwort: ")
        pw2 = getpass("Passwort wiederholen: ")
        if pw1 != pw2:
            print("Passwörter stimmen nicht überein\n")
            continue
        if len(pw1) < 6:
            print("Passwort zu kurz (mind. 6 Zeichen)\n")
            continue
        with open("passwort.hash", "w") as file:
            file.write(hash_passwort(pw1))
        print("\nPasswort gespeichert")
        input("Enter drücken um fortzufahren")
        break


def passwort_pruefen():
    gespeicherter_hash = open("passwort.hash").read().strip()
    for _ in range(3):
        eingabe = getpass("Passwort eingeben: ")
        if hash_passwort(eingabe) == gespeicherter_hash:
            print("Zugang gewährt")
            return True
        else:
            print("Falsches Passwort")
    print("Zu viele Fehlversuche")
    return False


if not os.path.exists("passwort.hash"):
    passwort_erstellen()
else:
    if not passwort_pruefen():
        exit()

stunde = datetime.now().hour
if 5 <= stunde < 12:
    begruessung = "Guten Morgen"
elif 12 <= stunde < 18:
    begruessung = "Guten Tag"
else:
    begruessung = "Gute Nacht"

title = "Noder"
version = "0.1.0"

clear()
print("=" * 30)
print(f"{title} v{version}")
print("=" * 30)

logo = r"""
███╗   ██╗ ██████╗ ██████╗ ███████╗██████╗
████╗  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║██║  ██║█████╗  ██████╔╝
██║╚██╗██║██║   ██║██║  ██║██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝██████╔╝███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

print(logo)
print("=" * 40)
print(begruessung)

loading("Starte Noder")
time.sleep(0.5)

while True:
    clear()
    print("-" * 30)
    print("1) Notiz erstellen")
    print("2) Notiz löschen")
    print("3) Notizen durchsuchen")
    print("4) Schliessen")
    print("-" * 30)

    try:
        anzahl = len(open("notizen.txt").readlines())
    except FileNotFoundError:
        anzahl = 0

    uhrzeit = datetime.now().strftime("%H:%M")
    print(f"Notizen: {anzahl} | Uhrzeit: {uhrzeit}")

    auswahl = input("\nWählen sie aus: ")

    if auswahl == "1":
        notiz = input("Gib deine Notiz ein: ")
        zeitstempel = datetime.now().strftime("%d.%m.%Y %H:%M")
        with open("notizen.txt", "a") as file:
            file.write(f"[{zeitstempel}] {notiz}\n")
        loading("Speichere Notiz")
        input("Notiz gespeichert – Enter drücken")

    elif auswahl == "2":
        try:
            with open("notizen.txt", "r") as file:
                notizen = file.readlines()
            if not notizen:
                print("Keine Notizen vorhanden.")
            else:
                for i, n in enumerate(notizen, start=1):
                    print(f"{i}. {n.strip()}")
                nr = int(input("\nNummer löschen: ")) - 1
                del notizen[nr]
                with open("notizen.txt", "w") as file:
                    file.writelines(notizen)
                print("Notiz gelöscht")
        except (FileNotFoundError, ValueError, IndexError):
            print("Ungültige Eingabe")
        input("Enter drücken")

    elif auswahl == "3":
        try:
            with open("notizen.txt", "r") as file:
                notizen = file.readlines()
            suchwort = input("Suchbegriff: ").lower()
            gefunden = False
            print("\nTreffer:")
            for i, n in enumerate(notizen, start=1):
                if suchwort in n.lower():
                    print(f"{i}. {n.strip()}")
                    gefunden = True
            if not gefunden:
                print("Keine Treffer gefunden.")
        except FileNotFoundError:
            print("Keine Notizen vorhanden.")
        input("\nEnter drücken")

    elif auswahl == "4":
        loading("Beende Programm")
        break

    else:
        print("Ungültige Eingabe")
        input("Enter drücken")
