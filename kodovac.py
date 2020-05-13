class Kodovac:
    # "klic": "hodnota"
    slovnik_sifer = {
        "a": "9",
        "b": "-",
        "c": "l",
        "d": "+",
        "e": "/",
        "f": "i",
        "g": "!",
        "h": "7",
        "i": "g",
        "j": "$",
        "k": "3",
        "l": "1",
        "m": "e",
        "n": "?",
        "o": "a",
        "p": "&",
        "q": "d",
        "r": "8",
        "s": "_",
        "t": "=",
        "u": "z",
        "v": "5",
        "w": "h",
        "x": "ks",
        "y": "2",
        "z": "p",
        " ": "c",
        ".": "s",
        ",": "(",
    }

    def sifrovat(self, text_k_sifrovani):
        rozlozeny_text = list(text_k_sifrovani)  # rozlozi text na jednotlive znaky
        zasifrovany_text = ""                    # ukladame prazdny string ("") do promene zasifrovany_text
        for i in range(len(rozlozeny_text)):     # cyklus, ktery prochazi seznam znaku
            znak = rozlozeny_text[i]             # vybere znak ze seznamu znaku(rozlozeny_text)
            sifra = self.slovnik_sifer.get(str(znak))  # na zaklade znaku dostaneme sifru ze zadefinovaneho slovniku
            zasifrovany_text += sifra            # postupne prirazuje do textu sifry
        return zasifrovany_text

    def desifrovat(self, text_k_desifrovani):   # tato metoda funguje na setjnem principu jako metoda "sifrovat" ale pouziva prehozene klice a hodnoty
        rozlozena_sifra = list(text_k_desifrovani)
        rozsifrovany_text = ""
        prehozeny_slovnik = self._prehozeni()
        for i in range(len(rozlozena_sifra)):
            sifra = rozlozena_sifra[i]
            znak = prehozeny_slovnik.get(sifra)
            rozsifrovany_text += znak
        return rozsifrovany_text

    def _prehozeni(self):  # v teto metode prehazuje klice a hodnoty (keys, values)
        klice = list(self.slovnik_sifer.keys())
        hodnoty = list(self.slovnik_sifer.values())
        prehozeny_slovnik = {}
        for i in range(len(klice)):
            prehozeny_slovnik[hodnoty[i]] = klice[i]
        return prehozeny_slovnik
