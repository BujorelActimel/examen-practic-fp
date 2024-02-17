import pytest
import random
from service import Service
from repo import Repo
from domain import Spectacol

def test_add_spectacol():
    file = "service/test_files/test_add.csv"
    service = Service(Repo(file))
    with open(file, "r") as f:
        lines = f.readlines()
        assert len(lines) == 0
        assert len(service.repo.spectacole) == 0
    
    service.add_spectacol(Spectacol(
        "titlu",
        "artist",
        "Comedie",
        3000,
    ))
    with open(file, "r") as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert len(service.repo.spectacole) == 1
    
    with open(file, "w") as f:
        f.write("")


def test_modify_spectacol():
    file = "service/test_files/test_modify.csv"
    service = Service(Repo(file))
    
    service.add_spectacol(Spectacol(
        "titlu",
        "artist",
        "Comedie",
        3000,
    ))
    assert service.repo.spectacole[0].durata == 3000
    
    service.modify_spectacol("titlu", "artist", "Comedie", 2000)
    assert service.repo.spectacole[0].durata == 2000

    with pytest.raises(ValueError):
        service.modify_spectacol("inexistent", "inexistent", "Comedie", 2000)
    
    with open(file, "w") as f:
        f.write("")


def test_generate_name():
    random.seed(1)
    file = "service/test_files/test_generate.csv"
    service = Service(Repo(file))

    assert service.generate_name() == "xalatotoja borubolexana"


def test_generate_spectacole():
    random.seed(1)
    file = "service/test_files/test_generate.csv"
    service = Service(Repo(file))

    assert str(service.generate_spectacole(1)[0]) == "xalatotoja borubolexana,bubojobuk owepekomaruz,Comedie,1761"

    with open(file, "r") as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert len(service.repo.spectacole) == 1

    with open(file, "w") as f:
        f.write("")


def test_export_spectacole():
    file = "service/test_files/test_export.csv"
    file_result = "service/test_files/test_export_result.csv"
    service = Service(Repo(file))
    service.add_spectacol(Spectacol(
        "titlu2",
        "artist2",
        "Comedie",
        3000,
    ))
    service.add_spectacol(Spectacol(
        "titlu2",
        "artist1",
        "Comedie",
        3000,
    ))
    service.add_spectacol(Spectacol(
        "titlu",
        "artist",
        "Comedie",
        3000,
    ))

    service.export_spectacole(file_result)

    with open(file_result, "r") as f:
        lines = f.readlines()

        assert lines[0].strip() == "titlu,artist,Comedie,3000"
        assert lines[1].strip() == "titlu2,artist1,Comedie,3000"
        assert lines[2].strip() == "titlu2,artist2,Comedie,3000"
        
    with open(file_result, "w") as f:
        f.write("")

    with open(file, "w") as f:
        f.write("")
