"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Vít Kamenický
email: vit.kamenicky@gmail.com
discord: Wiky_K
"""

from task_template import TEXTS
# import textu ze souboru

jmeno = input("Uživatelské jméno: ")
heslo = input("Heslo: ")
uzivatel = {'bob': '123',
            "ann": "pass123",
            "mike": "password123",
            "liz": "pass123"}

oddelovac = (40 * "-")
# promena pro vypsaní dlouhé pomlčky o 40 znacích 

print(oddelovac)

if uzivatel.get(jmeno) == heslo: # podmínka aby uživatel zadal pouze existujíci účet
    print("Ahoj", jmeno, "výtej v mé aplikaci.","\nMám 3 texty k analýze")
else:
    print("Špatné jmeno nebo heslo \nUkončuji program")
    exit()

print(oddelovac)

Zadane_cislo = input("Zadej cislo od 1 do 3: ")
if not Zadane_cislo.isnumeric(): # podmínka když uživatel nezadá číslo, ale cokoliv jiného.
    print("Musíš zadat číslo ne text! \nUkončuji program")
    exit()

print(oddelovac)

vyber_textu = int(Zadane_cislo) # Převede na číslo

if 1 <= vyber_textu <= 3: # v podstatě funkce range, podmínka aby uživatel nazadal číslo v jinem něž zadaném rozsahu
    veta = (TEXTS[vyber_textu -1]).split() # funkce split rozdělí vetu místu mezer čárkami aby mohla být spočítána funkcí len
    print(len(veta)," slov ve větě")
else:
    print('Musis zadat číslo od 1 do 3!\nUkončuji program')
    exit()

veta_bez_znaku = [slovo.strip(",.!?") for slovo in veta] # funkce strip smaže z vety všechny zadané symboly, muselo se to udělat protože jinak nefungovala funkce isalpha, protože když byla za slovem ve vetě čárka, tak už funkce isalpha brala slovo, že není text. 
prvni_velka_pismena = [slovo for slovo in veta_bez_znaku if slovo.istitle() and slovo.isalpha()] # slovo s prvním velkym písmene a je text
print(len(prvni_velka_pismena), " začínajici slo velkým pismenem")
velka_pismena = [slovo for slovo in veta_bez_znaku if slovo.isupper() and slovo.isalpha()] # slovo psané cele velkými pismeny a je text
print(len(velka_pismena), " slova psaná velkými písmeny")
mala_pismena = [slovo for slovo in veta_bez_znaku if slovo.islower() and slovo.isalpha()] # slovo psane malími písmeny a je text
print(len(mala_pismena), " slov s malymi písmeny")
pocet_cisel = [cislo for cislo in veta_bez_znaku if cislo.isnumeric()] # počet čísel ve větě
print(len(pocet_cisel), " počet čísel")
soucet_cisel = [int(cislo) for cislo in pocet_cisel] 
print(sum(soucet_cisel), " součet čísel")

print(oddelovac)

print("{:<5}".format("DELKA"), "|", "{:^20}".format("VÝSKYT"), "|POČET")

print(oddelovac)

delka_slov = []
for i in veta_bez_znaku:
    delka_slova = len(i)
    delka_slov.append(delka_slova)
# spočíta písmena v každém slově ve větě, a append číslo přidá do proměné delka_slov

znak = "*"

delky = {}
for znaky in delka_slov:
    if znaky not in delky:
        delky[znaky] = 1
    else:
        delky[znaky] = delky[znaky] + 1
# projde každé číslo z delky_slov a zapíše do slovníku delky jako klíč slovníku a 
# když se vyskytne stejně dlouho slovo, 
# zapíše počet kolikrát se opakuje jako hodnotu slovníku

for klic, hodnota in sorted(delky.items()):
    print("{:<5}".format(klic), "|", "{:<20}".format(znak * hodnota), "|", hodnota)
# zarovná klíče a hodnoty pod sebe, aby se dal vytisknout graf