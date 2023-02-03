""" Megoldás"""





def pontszamitas(lapok: [int]):
        pontok: int = 0
        for i in range(len(lapok)):
                pontok += lapok[i]
        return pontok


def eredmeny(jatekosLapok: [int], gepLapok: [int]):
        jatekosPontok = pontszamitas(jatekosLapok)
        gepPontok = pontszamitas(gepLapok)
        if jatekosPontok > 21 or jatekosPontok < gepPontok:
                szoveg = "Játékos vesztett"
        elif gepPontok > 21 or jatekosPontok > gepPontok:
                szoveg = "Játékos gyözött"
        else:
                szoveg = "Döntetlen"
        return szoveg


"""tesztesetek"""


def jatekosVezstettTeszt():
        jatekosLista = [10, 3, 2, 7]
        gepLista = [6, 4, 3]
        kapott = eredmeny(jatekosLista, gepLista)
        vart = "Játékos vesztett"
        if kapott == vart:
                print("A teszt sikeres")
        else:
                print("A teszt megbukott")

def tesztek():
        jatekosVezstettTeszt()


tesztek()
