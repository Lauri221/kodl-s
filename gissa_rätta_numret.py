import random # tarvitaan random-kirjasto
from random import randint # tuodaan rardint, kun tarvitaan satunnainen kokonaisluku
from time import sleep # tuodaan sleep, jotta voidaan lisätä ruudun päivitykseen odotusaika

print("Välkommen till Gissningsspelet!") # tervetuloa arvauspeliin
print("Gissa numret mellan 1 och 100!") # käyttäjä arvaa numeron 1 - 100 välillä
print("Jag har valt ett nummer, och du har 10 försök att gissa det.") # 10 yritystä
print("Om du gissar rätt vinner du, annars förlorar du.") # oikea arvaus voittaa pelin
print("Lycka till!") # pökköä pesään

# määritellään funktio, joka pyörittää peliä
def arvauspeli():
    oikea_numero = randint(1, 100) # määritellään oikea vastaus
    yritykset = 10 # yritysten määrä

    for yritys in range(1, yritykset + 1): # looppi, mikä lisää yritysten määrään +1
        try:
            arvaus = int(input(f"Försök {yritys}/{yritykset} - Ge nummer: ")) # käyttäjä arvaa numeron
            
        except ValueError: # estetään käyttäjää antamasta muita kuin numeroita
            print("Varsågod och ange ett nummer.")
            ???? # 1: continue, 2: break, 3: pass, 4: return
        
        #jos käyttäjä arvaa oikein

        if arvaus == oikea_numero: # tarkastaa, jos arvaus on sama kuin oikea vastaus
            print("Gratulerar, gratulerar! Din gissning är rätt!") # käyttäjä arvaa oikein
            break #käyttäjä voittaa pelin, ohjelma päättyy

        # jos käyttäjä arvaa väärin

        ???? arvaus < oikea_numero: # ehtolause, joka tarkistaa onko käyttäjän arvaus pienempi kuin oikea vastaus ## 1: if, 2: elif, 3: else, 4: while
            print("För lågt!") # liian alhainen arvaus

        ????: # muussa tapauksessa ## 1: if, 2: elif, 3: else, 4: while
            print("För högt!") # liian korkea arvaus

        if yritys == yritykset: # määritellään mitä tapahtuu, jos yritykset loppuvat
            print(f"Förlåt, men du har använt 10 gissar! Rätta numret var {oikea_numero}.")
        ????(1) # odotetaan 1 sekunti käyttäjän arvausten välillä ## 1: sleep, 2: wait, 3: pause, 4: stop

# peli käyntiin
arvauspeli???? # 1: (), 2: [], 3: {}, 4: <>
