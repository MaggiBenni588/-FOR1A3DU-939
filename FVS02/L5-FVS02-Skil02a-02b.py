
# coding: utf-8

# In[8]:



# Magnús Benedikt Guðjónsson
# 2017-02-06
# L5-FVS02-Skil02a Skilaverkfni 2

# Skilgreinum breytuna ysta_lykkja 
# og gefum henni upphafsgildið ja og breytum því aldrei.
ysta_lykkja = 'ja'

# while lykkjan keyrir á meðan ysta_lykkja er == ja
while ysta_lykkja == 'ja':
    print() # Til að setja bil á milli liða.
    print("1. Heilatala")
    print("2. Peningar")
    print("3. Þríhyrningur")
    print("4. Útreikningur")
    print("5. Skilningur")
    print("6. Hætta")
    # Val notanda sem tala (int) til að geta notað tölu í samanburði.
    val = int(input("Hvað viltu gera?"))
    print() # Til að setja bil á milli liða.
    
    # 
    # # #Liður 1 - Heilatala
    # 
    #  **#Liður 1 - Heilatala** 
    # Skrifaðu forritskóða sem spyr notandann um að slá inn heiltölu. 
    # Forritið svarar síðan „þú hefur valið töluna:“ og síðan skrifast rétt tala út. 
    # Forritið spyr síðan notanda hvort hann vilji slá inn aðra heiltölu. 
    # Ef því er svarað játandi er vinnslan endurtekin þar til að notandi velur að slá ekki inn fleiri tölur.
    # 
    if val == 1:

        svar = 'já'
        while svar == 'já' :
            inn_heiltala = int(input('Sláðu inn heiltölu: '))
            print('Þú hefur valið töluna:', inn_heiltala)
            svar = input('Viltu slá inn aðra heiltölu? (Svara með já eða nei)')


    # # #Liður 2 - Peningar
    # 
    #  **#Liður 2 - Peningar** 
    # Skrifaðu forritskóða sem biður um upphæð í krónum og segir svo til um hvað það eru margir :5000kr seðlar
    # 1000kr seðlar
    # 500kr seðlar
    # 100kr mynt
    # 50kr mynt
    # 10 kr mynt
    # 5kr mynt
    # 1 kr mynt.
    # Það þarf að nota heiltöludeilingu og if setningar.
    # 
    # Dæmi: Sláðu inn upphæð í krónum: 16683
    #     Þetta gera:
    #     3 stk 5000kr
    #     1 stk 1000 kr
    #     1 stk 500 kr
    #     1 stk 100 kr
    #     1stk 50 kr
    #     3 stk 10 kr
    #     3 krónur
    elif val == 2:
        print('#Liður 2 - Peningar')
        inn_upphaed = int( input('Sláðu inn upphæð í krónum: ') )
        print('Þetta gera:')

        afgangur = inn_upphaed
        if int(inn_upphaed / 5000) >= 1:
            print(int(inn_upphaed / 5000),'stk 5000kr')
            afgangur = inn_upphaed % 5000

        if int(afgangur / 1000) >=1:
            print(int(afgangur / 1000),'stk 1000kr')
            afgangur = inn_upphaed % 1000

        if int(afgangur / 500) >=1:
            print(int(afgangur / 500),'stk 500kr')
            afgangur = inn_upphaed % 500

        if int(afgangur / 100) >=1:
            print(int(afgangur / 100),'stk 100kr')
            afgangur = inn_upphaed % 100

        if int(afgangur / 50) >=1:
            print(int(afgangur / 50),'stk 50kr')
            afgangur = inn_upphaed % 50

        if int(afgangur / 10) >=1:
            print(int(afgangur / 10),'stk 10kr')
            afgangur = inn_upphaed % 10

        if int(afgangur / 1) >=1:
            print(int(afgangur / 1),'stk 1kr')
            afgangur = inn_upphaed % 1

    # # # Liður 3 - Þríhyrningur
    # 
    #  **# Liður 3 - Þríhyrningur** 
    # Skrifaðu forrit sem biður notanda um að slá inn heiltölu á bilinu 1 – 9. 
    # Forritið teiknar svo á skjáinn þríhyrning með hliðarlengd jafnri tölunni sem slegin er inn,
    # Ef tala 5 er slegin inn teiknar forritið þessa mynd:
    # 
    # \*
    # 
    # \* \*
    # 
    # \* \* \*
    # 
    # \* \* \* \*
    # 
    # \* \* \* \* \*
    # 
    # Ef talan 8 er slegin inn teiknar forritið þessa mynd:
    # 
    # \*
    # 
    # \* \*
    # 
    # \* \* \*
    # 
    # \* \* \* \*
    # 
    # \* \* \* \* \*
    # 
    # \* \* \* \* \* \*
    # 
    # \* \* \* \* \* \* \*
    # 
    # \* \* \* \* \* \* \* \*
    elif val == 3:

        print('# Liður 3 - Þríhyrningur')
        inn_heiltala = int(input('Sláðu inn heiltölu á bilinu 1 - 9:'))

        # Svo að ekki sé margfaldað með 0 byrjum við í einum og bætum einum við enda-töluna.
        for fjoldi_stjarna in range(1, inn_heiltala+1):
            print('* ' * fjoldi_stjarna)


    # # # Liður 4 - Útreikningur
    # 
    #  **# Liður 4 - Útreikningur** 
    # Skrifaðu forrit sem biður notandann um að slá inn heiltölu. 
    # Virkni forrits er síðan þannig að forritið tekur töluna sem slegin er inn 
    # segjum t.d. ef talan 4 er slegin inn og margfaldar saman rununa 4 * 3 * 2 * 1.
    # Ef slegin er inn talan fjórir kemur þetta út:
    # 4 * 3 * 2 * 1 = 24.
    # Forritið margfaldar sem sagt saman talnarununa frá tölunni sem slegin er inn alveg niður í 1.
    # Annað dæmi, ef talan 6 er slegin inn reiknar forritið
    # 6 * 5 * 4 * 3 * 2 * 1 = 720.
    elif val == 4:

        print('# Liður 4 - Útreikningur')

        inn_heiltala = int(input('Sláðu inn heiltölu:'))

        utkoma = 1
        for fjoldi_talna in range(inn_heiltala, 1, -1):
            print(str(fjoldi_talna)+' * ', end='')
            utkoma = utkoma * fjoldi_talna

        print('1 =', utkoma)


        # # # Liður 5 - SKilningur
        # 
        #  **# Liður 5 - SKilningur** 
        # Útskýrðu með eigin orðum virkni eftirfarandi kóðabrota og afhverju niðurstaðan er sú sem hún er
        # Skilið þessu sem kommentum neðst í .py skjalinu ykkar undir lið 5
        # i = 0 while i != 10: i = i + 1 print (i)
        # i = 1 while i != 10: i = i + 2 print (i)

    elif val == 5:
        # Upphafsgildi á teljara set á 0.
        i = 0

        # Lykkja telur meðan i er ekki 10.
        while i != 10: 
            # Hækkum i um einn í hverri umferð.
            i = i + 1 
            # Prentum út i.
            print (i)
            
        print('Hér byrjar seinnihlutinn í 5. Skilingur.') # Til að setja bil á milli liða.
        # Upphafsgildi á teljara set á 1.
        i = 1

        # Lykkja telur meðan i er ekki 10,
        # þar sem við byrjum í 1 og hækkum 
        # um 2 í hverri umferð, verður i 9
        # og síðan 11, en aldrei 10. Þetta er 
        # því endalaus lykkja sem aldrei stoppar.
        while i != 10: 
            # Hækkum i um tvo í hverri umferð.
            i = i + 2 
            if i > 30: # Bæti við if i > 30 svo keyrsla stoppi.
                break
            # Prentum út i.
            print (i)
            
    elif val == 6:
        break

    else:
        print("Þú hefur ekki valið rétt.")

