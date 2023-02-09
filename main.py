""" Megoldás"""





def pontszamitas(lapok: [int]):
        pontok: int = 0
        for i in range(len(lapok)):
                pontok += lapok[i]
        return pontok


def eredmeny(jatekosLapok: [int], gepLapok: [int]):
        jatekosPontok = pontszamitas(jatekosLapok)
        gepPontok = pontszamitas(gepLapok)
        szoveg = ""
        if jatekosPontok > 21 and gepPontok > 21:
                szoveg = "Döntetlen"
        elif jatekosPontok > 21:
                szoveg = "Játékos vesztett"
        elif gepPontok > 21:
                szoveg = "Játékos gyözött"
        elif gepPontok < jatekosPontok:
                szoveg = "Játékos gyözött"
        elif gepPontok > jatekosPontok:
                szoveg = "Játékos vesztett"
        elif jatekosPontok == gepPontok:
                if len(jatekosLapok) > len(gepLapok):
                        szoveg = "Játékos vesztett"
                elif len(jatekosLapok) < len(gepLapok):
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

def dontetlenEgyeloPontKartya():
        jatekosLista = [10, 3]
        gepLista = [10, 3]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Döntetlen"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def dontetlen21():
        jatekosLista = [10, 11]
        gepLista = [10, 11]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Döntetlen"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")


def jatekosNyertTulmentTeszt():
        jatekosLista = [10, 6, 3]
        gepLista = [6, 10, 8]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos gyözött"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")


def jatekosNyertEgyenloTeszt():
        jatekosLista = [10, 9]
        gepLista = [3, 10, 6]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos gyözött"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def jatekosNyertNagyobbTeszt():
        jatekosLista = [10, 9]
        gepLista = [3, 10, 2]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos gyözött"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def gepNyertNagyobbTeszt():
        jatekosLista = [10, 6, 3]
        gepLista = [3, 10, 2, 5]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos vesztett"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def gepNyertTulmentTeszt():
        jatekosLista = [10, 6, 9]
        gepLista = [3, 10, 2, 5]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos vesztett"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def gepNyertegyenloTeszt():
        jatekosLista = [10, 6, 3]
        gepLista = [9, 10,]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos vesztett"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")





def tesztek():
        jatekosVezstettTulmentTeszt()
        jatekosVezstettEgyenloTeszt()
        jatekosVezstettKisebbTeszt()
        jatekosNyertTulmentTeszt()
        jatekosNyertEgyenloTeszt()
        jatekosNyertNagyobbTeszt()
        gepVezstettKisebbTeszt()
        gepVezstettTulmentTeszt()
        gepVezstettEgyenloTeszt()
        gepNyertNagyobbTeszt()
        gepNyertTulmentTeszt()
        gepNyertegyenloTeszt()
        dontetlenTulment()
        dontetlenEgyeloPontKartya()
        dontetlen21()


tesztek()
