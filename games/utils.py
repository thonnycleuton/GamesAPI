from enum import Enum


class ChoiceEnum(Enum):
    """classe Enum reponsavel por iterar sobre cada item de uma lista de objetos"""

    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)


class Genero(ChoiceEnum):
    """Fornece opcoes para generos """
    MALE = 'M'
    FEMALE = 'F'
