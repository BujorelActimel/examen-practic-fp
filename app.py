import os
from domain import Spectacol
from repo import Repo
from service import Service
from ui import UI

class App:
    def __init__(self, file_name):
        self.__repo = Repo(file_name)
        self.__service = Service(self.repo)
        self.__ui = UI()

    @property
    def repo(self):
        return self.__repo

    @property
    def ui(self):
        return self.__ui

    @property
    def service(self):
        return self.__service

    def run(self):
        while True:
            os.system("cls")
            self.ui.show_menu()

            cmd = input("\n>>> ")

            if cmd == "0":
                os.system("cls")
                print("La revedere")
                break
            
            elif cmd == "1":
                titlu, artist, gen, durata = self.ui.get_spectacol_input()

                self.service.add_spectacol(Spectacol(
                    titlu,
                    artist,
                    gen,
                    durata,
                ))
                self.ui.enter_to_continue("Spectacol adaugat cu succes")

            elif cmd == "2":
                titlu, artist, gen, durata = self.ui.get_spectacol_input()

                try:
                    self.service.modify_spectacol(titlu, artist, gen, durata)
                except ValueError as err:
                    self.ui.enter_to_continue(err)
                else:
                    self.ui.enter_to_continue("Spectacol modificat cu succes")

            elif cmd == "3":
                numar_spectacole = self.ui.int_input("Numar de spectacole: ")
                results = self.service.generate_spectacole(numar_spectacole)
                for spectacol in results:
                    print(spectacol)

                self.ui.enter_to_continue()

            elif cmd == "4":
                file_name = self.ui.string_input("Nume Fisier: ")
                self.service.export_spectacole(f"data/{file_name}")
                self.ui.enter_to_continue("Exportare Reusita")

            else:
                self.ui.enter_to_continue("Comanda Invalida")


if __name__ == "__main__":
    app = App("data/spectacole.csv")
    app.run()
