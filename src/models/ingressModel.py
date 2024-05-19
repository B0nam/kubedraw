class Ingress:
    def __init__(self, name: str):
        self.name = name
        self.services = []

    def __str__(self) -> str:
        return self.name
