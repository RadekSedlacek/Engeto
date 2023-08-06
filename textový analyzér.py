"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Radek Sedláček
email: radek.sedalcek13@email.cz
discord: elvinek
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

oddeleni = "----------------------------------------"
uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}


# Přihlášení
uzivatel = input("username:")   
# Nechávám case sensitive
if uzivatel in uzivatele:
    heslo = input("password:")
    if heslo == uzivatele.get(uzivatel):
        print (oddeleni)
        print (f"Welcome to the app, {uzivatel} \nWe have 3 texts to be analyzed.")
        print (oddeleni)
    else:
        print ("wrong password, terminating the program..")
        quit()
else:
    print ("unregistered user, terminating the program..")
    quit()

# Výběr textu
text = input("Enter a number btw. 1 and 3 to select: ")
if text.isnumeric() == False:
    print ("That is not a number, terminating the program..")
    quit()
else:
    text = int(text)
    if text > 0 and text < 4:   
        volba = TEXTS[text -1]
        print(oddeleni)
    else:
        print ("That is not a number I have in store, terminatign the program..")
        quit()

# statistika - počet slov


vsechno = volba.split()
slova = []
for slovo in vsechno:
    slova.append(slovo.strip(".,:;"))

print (f"There are {len(slova)} in the selected text")

capital = []
velka = []
mala = []
cisla = []

for slovo in slova:
    # statistika - začínající velkým pismenem
    if slovo.istitle():
        capital.append(slovo)
    # statistika - velká slova
    if slovo.isupper():
        velka.append(slovo)
    # statistika - malá slova
    if slovo.islower():
        mala.append(slovo)
    # statistika - čísla
    if slovo.isnumeric():
        cisla.append(slovo)
        
print (f"There are {len(capital)} titlecase words.")
print (f"There are {len(velka)} uppercase words.")
print (f"There are {len(mala)} lowercase words.")
print(f"There are {len(cisla)} numeric strings.")

# statistika - součet
int_cisla = []
for slovo in cisla:
    int_cisla.append(int(slovo))

soucet = 0
for cislo in int_cisla:
    soucet = soucet + cislo
print (f"The sum of all the numbers {soucet}")

# halvička výskytů
print (oddeleni)
print (f"LEN|{'OCCURRENCES':^17}|NR.")

# rozdělit slova podle délky do slovníku

delka_slov = {}
for slovo in slova:
    delka = len(slovo)
    if delka in delka_slov:
        delka_slov[delka] +=1
    else:
        delka_slov[delka] = 1

# vypsat statistiku
for klíč, hodnota in sorted(delka_slov.items()):
    print(f"{str(klíč).rjust(3)}|{'*' * hodnota:17s}|{hodnota}")
