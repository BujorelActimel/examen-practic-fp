import random
from domain import Spectacol


class Service:
    def __init__(self, repo):
        self.__repo = repo

    @property
    def repo(self):
        return self.__repo

    def add_spectacol(self, spectacol: "Spectacol"):
        """
        adauga un spectacol in lista cu spectacole al 
        repository-ului si salveaza in fisier

        params: spectacol: Spectacol
        returns: None
        raises: None
        """
        self.repo.spectacole.append(spectacol)
        self.repo.save_data()

    def modify_spectacol(self, titlu, artist, gen, durata):
        """
        Cauta in lista cu spectacole un spectacol cu un anumit titlu
        si artist si il modifica si salveaza in fisier daca il gaseste

        params: 
            titlu: str
            artist: str
            gen: str
            durata: int
        returns: None
        raises: ValueError, daca nu gaseste spectacolul
        """
        for spectacol in self.repo.spectacole:
            if spectacol.titlu == titlu and spectacol.artist == artist:
                spectacol.gen = gen
                spectacol.durata = durata
                self.repo.save_data()
                return
    
        raise ValueError("Spectacolul nu a fost gasit")

    def generate_name(self):
        """
        Genereaza un nume de forma '**** ****' cu fiecare dintre
        parti putand sa aibe intre 9 si 12 caractere si care alterneaza
        vocalele cu consoanele

        params: 
        returns: name: str
        raises: None
        """
        vocale = "aeiou"
        consoane = "bcdfghjklmnpqrstvwxyz"
        name = ""
        vocala = False
        for _ in range(random.randint(9, 12)):
            if vocala:
                name += random.choice(vocale)
            else:
                name += random.choice(consoane)
            vocala = not vocala

        name += " "

        for _ in range(random.randint(9, 12)):
            if vocala:
                name += random.choice(vocale)
            else:
                name += random.choice(consoane)
            vocala = not vocala
        
        return name

    def generate_spectacole(self, numar_spectacole):
        """
        Genereaza spectcaole random

        params: numar_spectacole: int
        returns results: List[Spectacol]
        raises: None
        """
        results = []
        for _ in range(numar_spectacole):
            titlu = self.generate_name()
            artist = self.generate_name()
            gen = random.choice(["Comedie", "Concert", "Balet", "Altele"])
            durata = random.randint(1000, 5000)

            spectacol = Spectacol(
                titlu,
                artist,
                gen,
                durata,
            )

            results.append(spectacol)
            self.add_spectacol(spectacol)
        return results

    def export_spectacole(self, file_name):
        """
        Exporteaza spectacolele in ordine alfabetica
        in funcie de artist si titlu intr-un fisier

        params: file_name: int
        returns: None
        raises: None
        """
        spectacole = sorted(self.repo.spectacole, key=lambda x: (x.artist, x.titlu))
        with open(file_name, "w") as f:
            for spectacol in spectacole:
                f.write(str(spectacol) + "\n")
