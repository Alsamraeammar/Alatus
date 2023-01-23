#SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTN LASKEMISEEN
#=========================================================

# Muuttujat

#kysytään käyttäjältä tiedot
pituus_teksti = input('kuinkka pitkä olet (cm) ') 
paino_teksti = input('kuinka paljon painat (kg) ')
ika_teksti = input('kuinka vanha olet:')
sukupuoli_teksti = input('Sukupuoli mies, vastaa 1, nainen vastaa 0: ')

# Muutetaan vastaukset liukuluvuiksi
pituus = float (pituus_teksti)
paino = float(paino_teksti)
ika = float (ika_teksti)
sukupuoli= float(sukupuoli_teksti)


# Määritellä funktio painondeksin laskeentaan
def laske_bmi(paino, pituus):
    """Laskee painoindeksin (BMI) 

    Args:
        paino (float): paino (kg)
        pituus (float): pituus (cm)

    Returns:
    float: painoindeksin desimaalin tarkkuudella
    """
    pituus = pituus / 100 # muuteaan pituus metreiksi
    bmi = paino / pituus**2
    bmi = round(bmi, 1)
    return bmi

def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """_summary_

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1= > mies,0= > nainen

    Returns:
        _type_: _description_
        float kehon rasvaprosentti (aikuinen)
    """
    rasvaprosentti  = 1.20 * bmi + 0.23 * ika - 10.8 * sukupuoli -5.4
    rasvaprosentti = round (rasvaprosentti)
    return rasvaprosentti 

def lapsen_rasvaprosentti():


oma_bmi = laske_bmi(paino, pituus)
oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)

print('painoindeksisi on', oma_bmi, 
      'ja kehon rasvaprosentti on', oma_rasvaprosentti)


