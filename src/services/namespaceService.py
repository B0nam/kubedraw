from services.kubernetesService import KubernetesService
from services.resourceService import ResourceService
from models.namespaceModel import Namespace

class NamespaceService:
    def __init__(self, kubernetes_service):
        self.kubernetes_service = kubernetes_service
        self.resources_service = ResourceService(self.kubernetes_service)

    def generate_namespace_obj(self, namespace: str) -> Namespace:
        return self.resources_service.map_resources(namespace)