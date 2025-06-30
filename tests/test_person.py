from begins import Person

import pytest 

@pytest.fixture
def person():
    return Person("Rahul Shelke", 26, jobs=["Software Engineer"])

def test_init(person: Person):
    assert person.name == "Rahul Shelke"
    assert person.age == 26
    assert person.jobs == ["Software Engineer"]

def test_forname(person: Person):
    assert person.forname == "Rahul"

def test_surname(person: Person):
    assert person.surname == "Shelke"

def test_celebrate_birthday(person: Person):
    person.celebrate_birthday()
    assert person.age == 27

def test_add_job(person: Person):
    person.add_job("Zookeeper")
    assert person.jobs == ["Software Engineer", "Zookeeper"]