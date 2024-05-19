class Service:
    def __init__(self, name: str):
        self.name = name
        self.deployment = None
        self.pods = []

    def __str__(self) -> str:
        return self.name
