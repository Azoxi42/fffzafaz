import os

title="""Golden-Multitools"""

menu_items = {
    "1": ("Emails generator", "Emails.py"),
    "2": ("Ip", "IPschear.py"),
    "3": ("Quitter", None)
}

def afficher_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(title)
    print("")
    for key, (label, _) in menu_items.items():
        print(f"[{key}] {label}")
    print("")

def main():
    while True:
        afficher_menu()
        choix = input("Choix ").strip()
        if choix in menu_items:
            nom_script = menu_items[choix][1]
            if nom_script is None:
                print("")
                break
            os.system(f"python {nom_script}")
        else:
            print("")
            input("")

if __name__ == "__main__":
    main()