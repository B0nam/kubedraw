from resources.models.serviceModel import Service

class Ingress:
    def __init__(self, name: str):
        self.name = name
        self.services = []

    def add_service(self, service: Service):
        self.services.append(service)

    def __str__(self) -> str:
        return self.name
