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
                return "Játékos vesztett"
        elif gepPontok > 21 or jatekosPontok > gepPontok:
                return "Játékos gyözött"
        else:
                return "Döntetlen"


"""tesztesetek"""



