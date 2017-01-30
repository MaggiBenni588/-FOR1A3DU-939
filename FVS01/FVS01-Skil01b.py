
# coding: utf-8

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

# In[4]:

notendaNafn = input('Ritaðu inn nafnið þitt: ')
print ("Velkomin í áfangann FOR1TÖ3AU " + notendaNafn + " Þetta verður skemmtileg önn, ég hlakka til að læra forritun.")


# ***\#Liður 2 Formatta kommutölu:***
# 
# Forritið biður notanda að slá inn kommutölu með þrem aukastöfum og svarar síðan ”**Þú hefur valið töluna**: ” og síðan birtist talan sem slegin var inn með **einum aukastaf**.

# In[7]:

kommutala = float(input('Sláðu inn kommutölu með þrem aukastöfum (notaðu . í stað ,): '))
print('Þú hefur valið töluna: ' + str(format(kommutala, '.1f')))


# ***\#Liður 3 - Reikniaðgerðir:***
# 
# Forritið biður um tvær heiltölur, það á síðan að margfalda þessar tvær tölur saman og birta útkomuna á skjáinn.
# 
# Svo á forritið að draga fyrri töluna sem sleginn var inn frá þeirri seinni og skrifa þá útkomu á skjáinn.

# In[34]:

heiltala1 = float(input('Sláðu inn heiltölu 1: '))
heiltala2 = float(input('Sláðu inn heiltölu 2: '))
print('Margfaldaðar saman gerir: ' + str(format((heiltala1 * heiltala2), 'n')))
print('Mismunur þeirra er: ' + str(format((heiltala2 - heiltala1), 'n')))


# ***\#Liður 4- Meðalaldur:***
# 
# Hannið forrit sem biður um aldur á þremur einstaklingum. Síðan á forritið að reikna út meðalaldur þeirra og birta hann með einum aukastaf

# In[48]:

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

# In[6]:

# Það er óljóst hvort þessi liður á að skila minnstu tölunni eða tölunni í miðjunni. 
# ToDo ekki búinn með þennan lið.
heiltala1 = float(input('Sláðu inn heiltölu 1: '))

heiltala2 = float(input('Sláðu inn heiltölu 2: '))
if heiltala1 == heiltala2:
    print('Heiltala 2 má ekki vera sú sama og heiltala 1.') 
    heiltala2 = float(input('Sláðu inn aðra tölu fyrir heiltölu 2: '))

heiltala3 = float(input('Sláðu inn heiltölu 3: '))
if heiltala3 == heiltala1 or heiltala3 == heiltala2:
    print('Það má ekki nota sömu heiltölu oft við keyrslu þessa forrits.')
    heiltala3 = float(input('Sláðu inn aðra tölu fyrir heiltölu 3: '))

if heiltala3 == heiltala1 or heiltala3 == heiltala2 or heiltala1 == heiltala2:
    print('Það má ekki nota sömu heiltölu oft við keyrslu þessa forrits. Vinsamlega byrjaðu upp á nýtt.')
    # ToDo setja inn brake skipun hér þarf að fletta upp hvernig hún er.

midjutala = heiltala1
if heiltala2 > heiltala1:
    midjutala = heiltala2
if heiltala3 > midjutala
    midjutala = heiltala3


# ***\#Liður 6 - Árstíðir:***
# 
# \#Hérna notum við skilyrðissetningur (if-elif-else)
# 
# Forritið spyr um númer mánaðar. Forritið skrifar síðan út eftirfarandi:
# 
# Ef sleginn er inn talan 1‐3 skrifast út **”Nú er daginn tekið að lengja.”**
# Ef sleginn er inn talan 4‐5 skrifast út **”Vorið er komið og grundirnar gróa.”**
# 
# Ef sleginn er inn talan 6‐8 skrifast út **”Núna er sumarið komið með blóm í haga.”**
# 
# Ef sleginn er inn talan 9‐10 skrifast út **”Núna er haustið gengið í garð.”**
# 
# Ef sleginn er inn talan 11‐12 **”Núna styttist í jólin”**
# 
# Ef sleginn er inn talan sem er 0 eða minni eða 13 og hærri á að skrifa **“Rangur innsláttur”.**

# **\# Lidur 7:Talnabil**
# 
# \#Hérna notum við skilyrðissetningur (if-elif-else)
# 
# Forritið biður notanda um tölu sem er lægri en 0 eða hærri en 10.
# 
# Ef notandi slær inn tölu frá 0 til 10 (að þeim meðtöldum) birtist "Þessi tala er ekki lægri en núll eða hærri en 10". Annars svarar forritið "Vel gert!".

# ***\#Liður 8 að kveðja:***
# 
# Að lokum birtist á skjánum:
# 
# **Gaman að geta aðstoðað þig við þessa útreikninga –** *nafn notandans***-. **

# In[15]:

'{:<30}'.format('left aligned')


# In[16]:

'{:^30}'.format('centered')


# In[17]:

'{:*^30}'.format('centered')  # use '*' as a fill char

