#SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTN LASKEMISEEN
#=========================================================

# Muuttujat
pituus_teksti = input('kuinkka pitkä olet (cm) ') #kysytään käyttäjältä
paino_teksti = input('kuinka paljon painat (kg) ')#kysytään käyttäjältä
pituus = float (pituus_teksti)
paino = float(paino_teksti)

'''
pituus_metreina = pituus / 100

# Lasketaan painoindeksi (BMI)
bmi = paino / pituus_metreina **2

print('Painoindeksisi on', bmi)

'''
# Määritellä funktio painondeksin laskeentaan
def laske_bmi(paino, pituus):
    pituus = pituus / 100 # muuteaan pituus metreiksi
    bmi = paino / pituus**2
    return bmi

bmi = laske_bmi(paino, pituus=)

print('Laskin painoindeksin se on', bmi)

