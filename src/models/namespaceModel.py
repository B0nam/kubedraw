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

    def __str__(self) -> str:
        namespace_str = f'{self.name} {{\n'
        for pod in self.pods:
            namespace_str += f'\t{pod.name}[icon: k8s-pod]\n'
        for deployment in self.deployments:
            namespace_str += f'\t{deployment.name}[icon: k8s-deploy]\n'
        for service in self.services:
            namespace_str += f'\t{service.name}[icon: k8s-svc]\n'
        for ingress in self.ingresses:
            namespace_str += f'\t{ingress.name}[icon: k8s-ing]\n'
        namespace_str += "}"
        return namespace_str
