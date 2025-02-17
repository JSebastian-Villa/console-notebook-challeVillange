# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime


class Note:
    HIGH : str = "HIGH"
    MEDIUM : str = "MEDIUM"
    LOW : str = "LOW"

    def __init__(self,code: str, title: str, text: str, importance : str, creation_date: datetime ):

        self.code = code
        self.title = title
        self.text = text
        self.importante = importance
        self.tags : list[str] = []

    def add_tag(self, tag: str ):
        if tag not in self.tags:
            self.tags.append(tag)
        else:
            print(f"La etiqueta ingresada ya existe!")










