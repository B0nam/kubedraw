class Pod:
    def __init__(self, name: str):
        self.name = name
        self.deployment = None

    def __str__(self) -> str:
        return self.name
