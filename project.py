ukoly =[]

def hlavni_menu():
    print("\nSprávce úkolů - Hlavní menu \n\n1. Přidat nový úkol \n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu")
    volba=int(input("Vyberte možnost (1-4):\n"))
    if volba == 1:
        pridat_ukol()
    elif volba == 2:
        zobrazit_vsechny_ukoly()
        hlavni_menu()
    elif volba == 3:
        odstranit_ukol()
    elif volba == 4:
        print("Konec programu")
    else:
        print("\nToto je špatná volba, prosím, opakujte výběr:")
        input("Vyberte možnost (1-4):\n")

def pridat_ukol():
    nazev =input("\nZadejte název úkolu:")
    popis =input("Zadejte popis úkolu:")
    if nazev == "" or popis == "":
        print("\nNevyplnili jste název nebo popis úkolu, opakujte akci:\n")
        pridat_ukol()
    ukol={"Název":nazev,"Popis":popis}
    ukoly.append(ukol)

    hlavni_menu()
    

def zobrazit_vsechny_ukoly():
    if not ukoly:
        print("\nŽádný úkol není k dispozici:\n")
        hlavni_menu()
    print("\nSeznam úkolů:\n")
    for i in range(len(ukoly)):
        print(f"{i+1}) {ukoly[i]['Název']} - {ukoly[i]['Popis']}")

def odstranit_ukol():
    zobrazit_vsechny_ukoly()   
    ukol_k_odstraneni=int(input("\nZadejte číslo úkolu k odstranění:\n"))
    if ukol_k_odstraneni > 0 and ukol_k_odstraneni <= len(ukoly):
        ukoly.pop(ukol_k_odstraneni-1)
        print("\nÚkol č. " + str(ukol_k_odstraneni) + " byl odstraněn.")
    else:
        print ("\nNeexistující úkol, zadejte číslo úkolu k odstranění znovu.\n")
        odstranit_ukol()
    hlavni_menu()



hlavni_menu()