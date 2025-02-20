ukoly =[]

def hlavni_menu():
    print("1. Přidat nový úkol \n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu")
    volba=int(input("Vyberte možnost (1-4): "))
    if volba == 1:
        pridat_ukol()
    elif volba == 2:
        zobrazit_vsechny_ukoly()
    elif volba == 3:
        odstranit_ukol()
    elif volba == 4:
        print("Konec programu")
    else:
        print("Toto je špatná volba, prosím, opakujte výběr")
        input("Vyberte možnost (1-4)")

def pridat_ukol():
    nazev =input("Zadejte název úkolu")
    popis =input("Zadejte popis úkolu")
    if nazev == "" or popis == "":
        print("Zadali jste prázdný vstup")
        pridat_ukol()
    ukol={"Název":nazev,"Popis":popis}
    ukoly.append(ukol)
    

def zobrazit_vsechny_ukoly():
    if not ukoly:
        print("Žádný úkol není k dispozici")
    for i in range(len(ukoly)):
        print(f"{i+1}) {ukoly[i]['Název']} - {ukoly[i]['Popis']}")

def odstranit_ukol():
    zobrazit_vsechny_ukoly()
    ukol_k_odstraneni=input("Zadejte číslo úkolu k odstranění")
    ukoly.pop(ukol_k_odstraneni)



# hlavni_menu()
# zobrazit_vsechny_ukoly()
pridat_ukol()
zobrazit_vsechny_ukoly()