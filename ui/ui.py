class UI:
    def show_menu(self):
        print("Comenzi:")
        print("1. Adauga spectacol")
        print("2. Modifica spectacol")
        print("3. Generati spectacol")
        print("4. Exporta spectacole")
        print("0. Exit")

    def enter_to_continue(self, msg=""):
        input(f"{msg}\nApasati ENTER pentru a continua")

    def gen_input(self, msg=""):
        while True:
            gen = input(msg)
            try:
                assert gen in ["Comedie", "Concert", "Balet", "Altele"]
            except AssertionError:
                raise ValueError("Gen invalid, trebuie sa fie unul din: Comedie, Concert, Balet, Altele")
            else:
                return gen
    
    def int_input(self, msg=""):
        while True:
            res = input(msg)
            try:
                res = int(res)
                assert res > 0
            except ValueError:
                raise ValueError("Input invalid, incearca un numar")
            except AssertionError:
                raise ValueError("Input invalid, incearca un numar pozitiv")
            else:
                return res

    def string_input(self, msg=""):
        while True:
            res = input(msg)
            try:
                assert res != ""
            except AssertionError:
                raise ValueError("Input invalid, text vid")
            else:
                return res

    def get_spectacol_input(self):
        while True:
            errors = []
            ans = []

            try:
                titlu = self.string_input("Introduceti titlu: ")
            except ValueError as err:
                errors.append(err)
            else:
                ans.append(titlu)

            try:
                artist = self.string_input("Introduceti artist: ")
            except ValueError as err:
                errors.append(err)
            else:
                ans.append(artist)

            try:
                gen = self.gen_input("Introduceti genul: ")
            except ValueError as err:
                errors.append(err)
            else:
                ans.append(gen)

            try:
                durata = self.int_input("Introduceti durata: ")
            except ValueError as err:
                errors.append(err)
            else:
                ans.append(durata)

            if errors:
                for err in errors:
                    print(err)
            else:
                return ans
