# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:41:01 2021

@author: au100440
"""

"""
Flow control og boolske udtryk

"""
# Boolske værdier True/False og boolske operatorer er opkaldt efter matematiken og logikeren George Boole 
# Boolske værdier er en data type, der kun har to mulige værdier True (sand) eller False (falsk)
## Husk at skrive True og False med stort!
# Boolske operatorer er logiske operatorer (and, or, not), hvis output altid har den ene værdierne True og  False
# Sammenligningsoperatorer har også altid enten værdien True eller False
# Der er seks forskeellige sammenligningsoperatorer.
## == og != (lig med/ikke-lig med)
## < og > (mindre end/større end)
## <= og >= (mindre end eller lig med/større end eller lig med)
### En tom streng " " samt værdierne 0 og 0.0 tæller som værdien False
### En streng samt alle andre talværdier tæller som True 
#### Kan bruges som genvej, men det kan hurtigt blive svært at læse koden

###EKSEMPEL 1 - if + else ###
"""
print('Hvor mange kopper kaffe drikker du om dagen?')
a = int(input()) # input er altids strings - derfor bruges int() til at konvertere inputtert til et heltal (integer)
if a == 4: # hvis denne betingelser er opfyldt (True), afvikles linjen nedenunder
    print('Dit forbrug er gennemsnitligt')
else:
    print("Dit forbrug er enten over eller under gennemsnittet")
"""
### EKSEMPEL 2 - comparison if + elif ###

"""
print('Hvor mange kopper kaffe drikker du om dagen?')
a = int(input())
if a == 4: # hvis denne betingelser er opfyldt (True), afvikles linjen nedenunder
    print('Dit forbrug er gennemsnitligt')
elif a < 4: # Hvis den første betingelse ikke er opfyldt (False), afvikles denne sekvens og så fremdeles
    print('Du bør drikke mere kaffe!')
elif a > 4:
    print('Du bør drikke mindre kaffe!')
"""


### EKSEMPEL 3 comparison if + elif + boolian ###
"""
print('Hvor mange kopper kaffe drikker du om dagen?')
a = int(input())
if a == 4 or a == 5: # hvis denne betingelser er opfyldt (True), afvikles linjen nedenunder
    print('Dit forbrug er gennemsnitligt')
elif a < 4: # Hvis den første betingelse ikke er opfyldt (False), afvikles denne sekvens og så fremdeles
    print('Du bør drikke mere kaffe!')
elif a > 5:
    print('Du bør drikke mindre kaffe!')
    
"""
### EKSEMPEL 4a for loop + if ###
"""
a = ["jeg", "du", "at", "på", "undervisningsforløb", "programmeringskursus"] # liste der indeholder ord
for ord in a:           # loop, der tjekker alle ord på listen ovenfor
    if len(ord) > 5:    # betingelse (condition) der skal være opfyldt
        print(ord)      # hvis betingelsen er opfykdt afvikles denne betingelse
"""

### EKSEMPEL 4b for loop + if ###
"""
a = ["jeg", "du", "at", "på", "undervisningsforløb", "programmeringskursus"] # liste der indeholder ord
for x in a:           # loop, der tjekker alle ord på listen ovenfor
    if len(x) > 5:    # betingelse (condition) der skal være opfyldt
        print(x)      # hvis betingelsen er opfykdt afvikles denne betingelse
"""
### EKSEMPEL 5 for loop + if + .append() ###
"""
a = ["jeg", "du", "at", "på", "undervisningsforløb", "programmeringskursus"] # liste der indeholder ord
b = []                  # opretter en tom liste
for ord in a:           # loop, der tjekker alle ord på listen ovenfor
    if len(ord) > 5:    # betingelse (condition) der skal være opfyldt
        b.append(ord)   # tilføjer ordene fra liste a til liste b, hvis de opfylder betingelsen
print(b)      # hvis betingelsen er opfykdt afvikles denne betingelse
        
"""
### EKSEMPEL 6 while-loop + .append() ###
"""
a = []
while len(a) <= 4:
    print("Tast dit navn:")
    a.append(input())
    print(a)
print("Der er lukket for tilmeldinger")
"""
### EKSEMPEL 7a while-loop + break + .append() ###
"""
a = []
while True: # kører uendeligt fordi betingelsen altid er True
    print("Tast dit navn:")
    a.append(input())
    if len(a) >= 5:
        break # afbryder det uendelige loop, hvos betingelsen ovenfor er opfyldt
print("Der er lukket for tilmeldinger")
"""
### EKSEMPEL 7b while-loop + continue + .append() ###
"""
aa = []
while True: # kører uendeligt fordi betingelsen altid er True
    print("Tast dit navn:")
    bb = input()
    if bb == "Ulf":
        continue
    aa.append(bb)
    print(aa)
"""
    
       

