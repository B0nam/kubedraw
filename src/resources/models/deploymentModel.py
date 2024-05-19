from resources.models.podModel import Pod

class Deployment:
    def __init__(self, name: str):
        self.name = name
        self.pods = []

    def add_pod(self, pod: Pod):
        self.pods.append(pod)
        pod.deployment = self

    def __str__(self) -> str:
        return self.name