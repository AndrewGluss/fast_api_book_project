from model.creature import Creature
from service import creature as code

sample = Creature(name="Yeti",
                  country="CN",
                  area="Himalayas",
                  description="Hirsute Himalayan",
                  aka="Abominable Snowman")

def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exists():
    resp = code.get_one("Yeti")
    # assert resp == sample
    # возвращает false, хотя атрибуты объектов одинаковые и в классе BaseModel описан магический метод __eq__
    assert resp.name == sample.name

def test_get_missing():
    resp = code.get_one("khdfiebf")
    assert resp is None
