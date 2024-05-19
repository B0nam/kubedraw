from services.kubernetesService import KubernetesService
from services.resourceService import ResourceService

class DiagramService:
    def __init__(self):
        self.kubernetes_service = KubernetesService()
        self.resources_service = ResourceService(self.kubernetes_service)

    def generate_diagram_schema(self) -> str:
        try:
            namespaces = self.kubernetes_service.get_namespaces()
            diagram_schema = ''
            for namespace in namespaces:
                namespace_obj = self.resources_service.map_resources(namespace)
                diagram_schema += str(namespace_obj) + '\n\n'
            return diagram_schema
        except Exception as e:
            print("[-] Error generating diagram schema:", e)
            raise
