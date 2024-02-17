from domain import Spectacol

def test_Spectacol():
    spectacol = Spectacol("titlu", "artist", "gen", 3000)
    assert spectacol.titlu == "titlu"
    assert spectacol.artist == "artist"
    assert spectacol.gen == "gen"
    assert spectacol.durata == 3000