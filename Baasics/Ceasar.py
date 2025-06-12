import random

abc = "ABCDEFGHIJKLMONPQRSTVWXYZabcdefghijklmnopqrstuvwxyz!. ABCDEFGHIJKLMONPQRSTVWXYZabcdefghijklmnopqrstuvwxyz!. "

Klartext = "Der Adler ist gelandet"

Zufaelliger_Schluessel = random.randint(0,20)

#print(Zufaelliger_Schluessel)

def verschluesseln(eingabe,schluessel):
    print("Eingabewort: ", eingabe)
    print("Schluessel", schluessel)

    VerschluesseltesWort = ""

    for i in range (0,len(eingabe)):

        BuchstabenIndex = abc.index(eingabe[i])
        
        VerschluesselterIndex = BuchstabenIndex + schluessel
        
        VerschluesseltesWort = VerschluesseltesWort + abc[VerschluesselterIndex]
        
        #print("Eingagsbuchstabe : " + eingabe[i])
        #print("Buchstabenindex : "+ str(BuchstabenIndex+1))
        #print("VerschluesselterIndex: "+str(VerschluesselterIndex+1))
        #print("VerschluesselterBuchstabe" + abc[VerschluesselterIndex])

    print(VerschluesseltesWort)

verschluesseln(Klartext,Zufaelliger_Schluessel)


