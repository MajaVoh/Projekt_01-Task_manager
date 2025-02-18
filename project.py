def hlavni_menu():
    print("1. Přidat nový úkol \n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu")
    input("Vyberte možnost (1-4): ")
    if input == 1:
        pridat_ukol()
    elif input == 2:
        zobrazit_vsechny_ukoly()
    elif input == 3:
        odstranit_ukol()
    elif input == 4:
        print("Konec programu")
    else:
        print("Toto je špatná volba, prosím, opakujte výběr")
        input("Vyberte možnost (1-4)")

def pridat_ukol():
    nazev =input("Zadejte název úkolu")
    popis =input("Zadejte popis úkolu")
    ukol={"Název":nazev,"Popis":popis}
    ukoly.append(ukol)



def zobrazit_vsechny_ukoly():
    print(ukoly)

def odstranit_ukol():
    zobrazit_vsechny_ukoly()
    ukol_k_odstraneni=input("Zadejte číslo úkolu k odstranění")
    ukoly.pop(ukol_k_odstraneni)


ukoly = [
    {"Název": "Ukol jedna", "Popis": "Popis ukolu jedna"},
    {"Název": "Ukol dva", "Popis": "Popis ukolu dva"},
    {"Název": "Ukol tri", "Popis": "Popis ukolu tri"},
]

# hlavni_menu()
zobrazit_vsechny_ukoly()
# pridat_ukol()