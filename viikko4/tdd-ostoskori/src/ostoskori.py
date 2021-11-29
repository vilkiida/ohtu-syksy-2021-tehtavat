from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._hinta = 0
        self._kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if self._kori == []:
            return 0
        else:
            maara = 0
            for ostos in self._kori:
                maara += ostos.lukumaara()
            return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for ostos in self._kori:
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        onjo = False
        for ostos in self._kori:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                onjo = True
        if not onjo:
            ostos = Ostos(lisattava)
            self._kori.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self._kori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                if ostos.lukumaara() == 1:
                    self._kori.remove(ostos)
                if ostos.lukumaara() > 1:
                    ostos.muuta_lukumaaraa(-1)


    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
