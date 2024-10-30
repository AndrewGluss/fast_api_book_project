from ..model.explorer import Explorer

_explorers = [
    Explorer(name="Claude Hande",
             country="FR",
             description="Scarce during full moons"),
    Explorer(name="Noah Weiser",
             country="DE",
             description="Myopic machete man")
    ]

def get_all() -> list[Explorer]:
    """Возврат всех исследователей"""
    return _explorers

def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def create(explorer: Explorer):
    """Добавление исследователя"""
    return explorer

def modify(explorer: Explorer):
    """Частичное изменение исследователа"""
    return explorer

def replace(explorer: Explorer):
    """Полная замена исследователя"""
    return explorer

def delete(name: str) -> bool:
    """Удаление записи о исследователе
    Возврат None, если запись существовала"""

    return None