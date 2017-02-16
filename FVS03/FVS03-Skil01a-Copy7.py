
# coding: utf-8

# In[12]:

# Magnús Benedikt Guðjónsson
# 2017-02-16
# Skilaverkefni 3-Random og Math
# Skráarnafn: FVS03-Skil0Xx-CopyL


# In[ ]:

import random

while True:
    print() # Til að hafa bil á milli liða.
    print(' 1: Veldi.')
    print(' 2: Teningakast.')
    print(' 3: Yatzi kast.')
    print(' 4: Talna flóð.')
    print(' 5: Hætta.')
    print() # Til að hafa bil á milli liða.
    
    val = int(input(' Veldu úr ofangeindum lista: '))
    
    if val == 1:
        print(' 1: Veldi.')
        innUpphafstala = int(input(' Sláðu inn upphafstölu:'))
        innLokatala = int(input(' Sláðu inn lokatölu:'))

        for teljari in range(innUpphafstala,innLokatala +1 ):
            thridjaVeldi = pow(teljari,3)
            print(' ', teljari, 'og', thridjaVeldi)
        print() # Til að hafa bil á milli liða.
        continue

    if val == 2:
        print(' 2: Teningakast.')
        tala = random.randint(1, 6)
        print( ' Upp kom talan', tala, end ='.')
        print() # Til að hafa bil á milli liða.
        continue

    if val == 3:
        print(' 3: Yatzi kast.')
        print(' Upp komu tölurnar: ', end ='')
        for teljari in range(5):
            tala = random.randint(1, 6)
            print(tala, end =' ')
        print() # Til að hafa bil á milli liða.
        continue
        
    if val == 4:
        print(' 4: Talna flóð.')
        fjoldiTalna = 0
        for teljari in range(250):
            tala = random.randint(25, 115)
            if tala == 73:
                break
            elif tala == 99:
                print('Talan 99 kom upp.')
                fjoldiTalna = fjoldiTalna + 1
            else:
                print( tala, end =' ')
                fjoldiTalna = fjoldiTalna + 1

        print(' Fjöldi birtra talana er:', fjoldiTalna) 
        print() # Til að hafa bil á milli liða.
        continue
        
    if val == 5:
        print(' 5: Hætta.')
        break
    
    else:
        print(' Þú hefur ekki valið rétt, veldu aftur.')

