class Namespace:
    def __init__(self, name):
        self.name = name
        self.deploys = []
        self.services = []
        self.ingresses = []

    def add_deploy(self, deploy):
        self.deploy.append(deploy)

    def add_service(self, service):
        self.service.append(service)

    def add_ingress(self, ingress):
        self.ingress.append(ingress)