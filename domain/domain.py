class Spectacol:
    def __init__(self, titlu, artist, gen, durata):
        self.__titlu = titlu
        self.__artist = artist
        self.__gen = gen
        self.__durata = durata

    def __str__(self):
        return f"{self.titlu},{self.artist},{self.gen},{self.durata}" 

    @property
    def titlu(self):
        return self.__titlu

    @property
    def artist(self):
        return self.__artist

    @property
    def gen(self):
        return self.__gen

    @property
    def durata(self):
        return self.__durata

    @gen.setter
    def gen(self, new_gen):
        self.__gen = new_gen

    @durata.setter
    def durata(self, new_durata):
        self.__durata = new_durata
