from repo import Repo
from domain import Spectacol

def test_save_data():
    file = "repo/test_files/test_save.csv"
    repo = Repo(file)

    with open(file, "r") as f:
        lines = f.readlines()
        assert len(lines) == 0

    repo.spectacole.append(Spectacol(
        "titlu",
        "artist",
        "Comedie",
        3000,
    ))

    repo.save_data()

    with open(file, "r") as f:
        lines = f.readlines()
        assert len(lines) == 2
    
    with open(file, "w") as f:
        f.write("")


def test_load_data():
    file = "repo/test_files/test_load.csv"
    repo = Repo(file)

    assert len(repo.spectacole) == 3
