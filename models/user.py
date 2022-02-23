class User:
    def __init__(self, user, id=0) -> None:
        self.user = user
        self.id = id

    def __repr__(self) -> str:
        return f"User('{self.user}', {self.id})"
