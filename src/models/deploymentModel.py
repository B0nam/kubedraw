class Deployment:
    def __init__(self, name: str):
        self.name = name
        self.pods = []

    def __str__(self) -> str:
        return self.name
