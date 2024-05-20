from models.podModel import Pod
from models.deploymentModel import Deployment
from models.serviceModel import Service
from models.ingressModel import Ingress

class Namespace:
    def __init__(self, name: str):
        self.name = name
        self.pods = []
        self.deployments = []
        self.services = []
        self.ingresses = []

    def add_pod(self, pod: Pod):
        self.pods.append(pod)

    def add_deployment(self, deployment: Deployment):
        self.deployments.append(deployment)

    def add_service(self, service: Service):
        self.services.append(service)

    def add_ingress(self, ingress: Ingress):
        self.ingresses.append(ingress)
