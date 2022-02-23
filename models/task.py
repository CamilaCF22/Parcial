class Task:
    def __init__(self, iduser, description, idstatus, id=0) -> None:
        self.iduser = iduser
        self.description = description
        self.idstatus = idstatus
        self.id = id

    def __repr__(self) -> str:
        return f"Task({self.iduser}, '{self.description}', {self.idstatus}, {self.id})"
