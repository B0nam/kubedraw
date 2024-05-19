from resources.models.deploymentModel import Deployment
from resources.models.podModel import Pod

class Service:
    def __init__(self, name: str):
        self.name = name
        self.deployments = []
        self.pods = []

    def add_pod(self, pod: Pod):
        self.pods.append(pod)

    def __str__(self) -> str:
        return self.name
