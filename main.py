""" Megoldás"""





def pontszamitas(lapok: [int]):
        pontok: int = 0
        for i in range(len(lapok)):
                pontok += lapok[i]
        return pontok


def eredmeny(jatekosLapok: [int], gepLapok: [int]):
        jatekosPontok = pontszamitas(jatekosLapok)
        gepPontok = pontszamitas(gepLapok)
        if jatekosPontok > 21:
                szoveg = "Játékos vesztett"
        elif gepPontok > 21:
                szoveg = "Játékos gyözött"
        else:
                szoveg = "Döntetlen"
        return szoveg


"""tesztesetek"""


def jatekosVezstettTulmentTeszt():
        jatekosLista = [10, 6, 8]
        gepLista = [6, 10]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos vesztett"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def jatekosVezstettEgyenloTeszt():
        jatekosLista = [10, 3, 3]
        gepLista = [6, 10]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos vesztett"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")
def jatekosVezstettKisebbTeszt():
        jatekosLista = [10, 3]
        gepLista = [6, 10]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos vesztett"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def gepVezstettKisebbTeszt():
        jatekosLista = [10, 6]
        gepLista = [3, 10]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos gyözött"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def gepVezstettTulmentTeszt():
        jatekosLista = [10, 6]
        gepLista = [10, 6, 8]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos gyözött"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def gepVezstettEgyenloTeszt():
        jatekosLista = [10, 6]
        gepLista = [10, 3, 3]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos gyözött"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def dontetlenTulment():
        jatekosLista = [10, 6, 7]
        gepLista = [10, 3, 3, 8]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Döntetlen"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def dontetlenEgyelo():
        jatekosLista = [10, 3]
        gepLista = [10, 3]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Döntetlen"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")




def tesztek():
        jatekosVezstettTulmentTeszt()
        jatekosVezstettEgyenloTeszt()
        jatekosVezstettKisebbTeszt()
        gepVezstettKisebbTeszt()
        gepVezstettTulmentTeszt()
        gepVezstettEgyenloTeszt()
        dontetlenTulment()
        dontetlenEgyelo()


tesztek()
