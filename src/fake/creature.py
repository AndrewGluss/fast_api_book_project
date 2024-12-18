from ..model.creature import Creature

_creatures = [
    Creature(name="Yeti",
             aka="Abominable Snowman",
             country="CN",
             area='Himalayas',
             description="Hirsute Himalayan"),
    Creature(name="Bigfoot",
             aka="Sasquatch",
             country="US",
             area='*',
             description="Yeti's Cousin Eddie")
]

def get_all() -> list[Creature]:
    """Возврат всех существ"""
    return _creatures

def get_one(name: str) -> Creature | None:
    """Возврат одного существа"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    """Добавление существа"""
    return creature

def modify(creature: Creature) -> Creature:
    """Частичное изменение запищи существа"""
    return creature

def replace(creature: Creature) -> Creature:
    """Полная замена записи существа"""
    return creature

def delete(name: str):
    """Удаление запищи существа: Возврат значения None если запись существовала"""
    return None