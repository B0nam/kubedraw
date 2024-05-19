from models.deploymentModel import Deployment
from models.podModel import Pod

class Service:
    def __init__(self, name: str):
        self.name = name
        self.deployment = None
        self.pods = []

    def set_deployment(self, deployment: Deployment):
        self.deployment = deployment

    def add_pod(self, pod: Pod):
        self.pods.append(pod)

    def __str__(self) -> str:
        return self.name
