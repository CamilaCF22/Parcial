class Status:
    def __init__(self, name, id=0) -> None:
        self.name = name
        self.id = id

    def __repr__(self) -> str:
        return f"Status('{self.name}', {self.id})"
