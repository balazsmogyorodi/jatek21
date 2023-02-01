""" Megoldás"""


def pontszamitas(jatekosLapok, gepLapok):
        jatekosPontok = 0
        gepPontok = 0
        eredmenyek = []
        for i in range(len(jatekosLapok)):
                jatekosPontok += jatekosLapok[i]
        eredmenyek.append(jatekosPontok)
        for i in range(len(gepLapok)):
                gepPontok += gepLapok[i]
        eredmenyek.append(gepPontok)
        return eredmenyek

def eredmeny(jatekosPontok, gepPontok):
        if jatekosPontok > 21:
                return "Játékos vesztett"
        elif gepPontok > 21:
                return "Játékos gyözött"
        else:
                return "Döntetlen"
        """tesztesetek"""

eredmenyek = pontszamitas()
jatekosPontok = eredmenyek[0]
gepPontok = eredmenyek[1]
eredmeny(jatekosPontok, gepPontok)

