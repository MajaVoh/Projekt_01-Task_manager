ukoly = []

def hlavni_menu():
    print("1. Přidat nový úkol \n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu")
    input("Vyberte možnost (1-4)")
    if input == 1:
        pridat_ukol()
        input ==2
        zobrazit_vsechny_ukoly()
        input ==3
        odstranit_ukol()
        input==4
        print("Konec programu")
    else:
        print("Toto je špatná volba, prosím, opakujte výběr")
        input("Vyberte možnost (1-4)")

hlavni_menu()

def pridat_ukol():
    nazev =input("Zadejte název úkolu")
    popis =input("Zadejte popis úkolu")
    ukoly.append(nazev)
pridat_ukol()

def zobrazit_vsechny_ukoly():
    print(ukoly())

def odstranit_ukol():
