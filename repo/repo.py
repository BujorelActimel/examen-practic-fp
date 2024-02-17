from domain import Spectacol

class Repo:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__spectacole = self.load_data()

    @property
    def file_name(self):
        return self.__file_name

    @property
    def spectacole(self):
        return self.__spectacole

    def load_data(self):
        """
        incarca si returneaza o lista cu spectacolele din fisier

        params: 
        returns: list
        raises: None
        """
        results = []
        with open(self.file_name, "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                titlu, artist, gen, durata = line.strip().split(",")
                results.append(Spectacol(titlu, artist, gen, durata))
        return results

    def save_data(self):
        """
        scrie in fisier toate spectacolele din repository
        
        params:
        returns: None
        raises: None
        """
        with open(self.file_name, "w") as f:
            f.write("titlu,artist,gen,durata\n")
            for spectacol in self.spectacole:
                f.write(str(spectacol) + "\n")
