from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

if __name__ == "__main__":
    creature1 = Creature(name="1", country="2", area="3", description="4", aka="5")
    creature2 = Creature(name="1", country="2", area="3", description="4", aka="5")

    print(creature1 == creature2)