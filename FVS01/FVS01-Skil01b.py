# coding: utf-8
# Magnús Benedikt Guðjónsson
# 2017-01-29
# FVS01-Skil01b Skilaverkfni 1


# ***Skilaverkefni 1 ***
#
# Verkefnið gildir 10% af lokaeinkunn og gilda allir liðir verkefnisins jafnt
#
# **\# muna að kommenta verkefnið VEL – einkunn verður lækkuð um tvo heila ef ekki er nægjanlega vel kommentað**
#
# Í þessu verkefni eru nokkrir liðir, settu \#comment sem afmarkar hvern lið.

# ***\#Liður 1 Notandi:***
#
# Forritið biður um nafn notanda og skrifar síðan út:
#
# "**Velkomin í áfangann FOR1TÖ3AU** “ síðan *nafn notand*a og síðan ". **Þetta verður** **skemmtileg önn, ég hlakka til að læra forritun."**

print('#Liður 1 Notandi:')
notendaNafn = input('Ritaðu inn nafnið þitt: ')
print ("Velkomin í áfangann FOR1TÖ3AU " + notendaNafn + ". Þetta verður skemmtileg önn, ég hlakka til að læra forritun.")


# ***\#Liður 2 Formatta kommutölu:***
#
# Forritið biður notanda að slá inn kommutölu með þrem aukastöfum og svarar síðan ”**Þú hefur valið töluna**: ” og síðan birtist talan sem slegin var inn með **einum aukastaf**.

print('#Liður 2 Formatta kommutölu:')
kommutala = float(input('Sláðu inn kommutölu með þrem aukastöfum (notaðu . í stað ,): '))
print('Þú hefur valið töluna: ' + str(format(kommutala, '.1f')))


# ***\#Liður 3 - Reikniaðgerðir:***
#
# Forritið biður um tvær heiltölur, það á síðan að margfalda þessar tvær tölur saman og birta útkomuna á skjáinn.
#
# Svo á forritið að draga fyrri töluna sem sleginn var inn frá þeirri seinni og skrifa þá útkomu á skjáinn.

print('#Liður 3 - Reikniaðgerðir:')
heiltala1 = float(input('Sláðu inn heiltölu 1: '))
heiltala2 = float(input('Sláðu inn heiltölu 2: '))
print('Margfaldaðar saman gerir: ' + str(format((heiltala1 * heiltala2), 'n')))
print('Mismunur þeirra er: ' + str(format((heiltala2 - heiltala1), 'n')))

# ***\#Liður 4- Meðalaldur:***
#
# Hannið forrit sem biður um aldur á þremur einstaklingum. Síðan á forritið að reikna út meðalaldur þeirra og birta hann með einum aukastaf

print('#Liður 4- Meðalaldur:')
einstaklingur1 = float(input('Sláðu inn aldur á einstakling 1: '))
einstaklingur2 = float(input('Sláðu inn aldur á einstakling 2: '))
einstaklingur3 = float(input('Sláðu inn aldur á einstakling 3: '))
medaltal = ((einstaklingur1 + einstaklingur2 + einstaklingur3)/3)
print('Meðalaldur þeirra er: ' + format(medaltal, '.1f'))
print('Meðalaldur þeirra reiknaður á annan hátt er: ' + format(((einstaklingur1 + einstaklingur2 + einstaklingur3)/3), '.1f'))

# ***\#Liður 5 Minnsta talan:***
#
# \#Hérna notum við skilyrðissetningur (if-elif-else)
#
# Forritið spyr um þrjár heiltölur.
#
# Passa að ekki sé slegin inn sama tala tvisvar sinnum.
#
# Forritið skrifar síðan út hver talnanna er í miðjunni.

# Það er óljóst hvort þessi liður á að skila minnstu tölunni eða tölunni í miðjunni.
# Ákvað því að gera bæði og stæðstu tölunni að auki.

print('#Liður 5 Minnsta talan:')

heiltala1 = int(input('Sláðu inn heiltölu 1: '))

heiltala2 = int(input('Sláðu inn heiltölu 2: '))
if heiltala1 == heiltala2:
    print('Heiltala 2 má ekki vera sú sama og heiltala 1.')
    heiltala2 = int(input('Sláðu inn aðra tölu fyrir heiltölu 2: '))

heiltala3 = int(input('Sláðu inn heiltölu 3: '))
if heiltala3 == heiltala1 or heiltala3 == heiltala2:
    print('Það má ekki nota sömu heiltölu oft við keyrslu þessa forrits.')
    heiltala3 = int(input('Sláðu inn aðra tölu fyrir heiltölu 3: '))

if heiltala3 == heiltala1 or heiltala3 == heiltala2 or heiltala1 == heiltala2:
    print('Það má ekki nota sömu heiltölu oft við keyrslu þessa forrits. Vinsamlega byrjaðu upp á nýtt.')
else:
    # prenta auða línu á milli inntaks og úttaks.
    print()

    minnstaTala = heiltala1
    if heiltala2 < heiltala1:
        minnstaTala = heiltala2
    if heiltala3 < minnstaTala:
        minnstaTala = heiltala3

    print('Minnsta talan er:', minnstaTala)

    staedstaTala = heiltala1
    if heiltala2 > heiltala1:
        staedstaTala = heiltala2
    if heiltala3 > staedstaTala:
        staedstaTala = heiltala3

    # Það væri hægt að sleppa næstu línu (kommenta út/eyða)
    # ef ekki mætti sjást að stæðsta talan er notuð til að
    # finna þá sem er í miðjunni.
    print('Stæðsta talan er:', staedstaTala)

    if heiltala1 != minnstaTala and heiltala1 != staedstaTala:
        midjuTala = heiltala1
    if heiltala2 != minnstaTala and heiltala2 != staedstaTala:
        midjuTala = heiltala2
    if heiltala3 != minnstaTala and heiltala3 != staedstaTala:
        midjuTala = heiltala3

    print('Talan í miðjunni er:', midjuTala)


# ***\#Liður 6 - Árstíðir:***
#
# \#Hérna notum við skilyrðissetningur (if-elif-else)
#
# Forritið spyr um númer mánaðar. Forritið skrifar síðan út eftirfarandi:
#
# Ef sleginn er inn talan 1-3 skrifast út **”Nú er daginn tekið að lengja.”**
#
# Ef sleginn er inn talan 4-5 skrifast út **”Vorið er komið og grundirnar gróa.”**
#
# Ef sleginn er inn talan 6-8 skrifast út **”Núna er sumarið komið með blóm í haga.”**
#
# Ef sleginn er inn talan 9-10 skrifast út **”Núna er haustið gengið í garð.”**
#
# Ef sleginn er inn talan 11-12 **”Núna styttist í jólin”**
#
# Ef sleginn er inn talan sem er 0 eða minni eða 13 og hærri á að skrifa **“Rangur innsláttur”.**

print('#Liður 6 - Árstíðir:')
numerMandadar = int(input('Sláðu inn númer mánaðar: '))

if numerMandadar >= 1 and numerMandadar <= 3:
    print('Nú er daginn tekið að lengja.')
if numerMandadar >= 4 and numerMandadar <= 5:
    print('Vorið er komið og grundirnar gróa.')
if numerMandadar >= 6 and numerMandadar <= 8:
    print('Núna er sumarið komið með blóm í haga.')
if numerMandadar >= 9 and numerMandadar <= 10:
    print('Núna er haustið gengið í garð.')
if numerMandadar >= 11 and numerMandadar <= 12:
    print('Núna styttist í jólin.')
if numerMandadar <= 0 or numerMandadar >= 13:
    print('Rangur innsláttur.')


# **\# Lidur 7:Talnabil**
#
# \#Hérna notum við skilyrðissetningur (if-elif-else)
#
# Forritið biður notanda um tölu sem er lægri en 0 eða hærri en 10.
#
# Ef notandi slær inn tölu frá 0 til 10 (að þeim meðtöldum) birtist "Þessi tala er ekki lægri en núll eða hærri en 10". Annars svarar forritið "Vel gert!".

print('#Lidur 7:Talnabil')
innTala = float(input('Sláðu inn tölu sem er lægri en 0 eða hærri en 10: '))
if (innTala >= 0 and innTala <= 10):
    print('Þessi tala er ekki lægri en núll eða hærri en 10')
else: print('Vel gert!')


# ***\#Liður 8 að kveðja:***
#
# Að lokum birtist á skjánum:
#
# **Gaman að geta aðstoðað þig við þessa útreikninga ** *-nafn notandans-* **. **

print('#Liður 8 að kveðja:')

print ("Gaman að geta aðstoðað þig við þessa útreikninga " + notendaNafn + ".")
