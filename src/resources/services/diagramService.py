from resources.services.kubernetesService import KubernetesService
from resources.services.resourceService import ResourceService
from resources.models.namespaceModel import Namespace

class DiagramService:
    def __init__(self):
        self.kubernetes_service = KubernetesService()
        self.resources_service = ResourceService(self.kubernetes_service)

    def generate_diagram_schema(self, namespace='None') -> str:
        try:
            if namespace == 'None':
                all_namespaces = self.kubernetes_service.get_namespaces()
                return '\n'.join([self._generate_namespace_schema(ns) for ns in all_namespaces])
            return self._generate_namespace_schema(namespace)
        except Exception as e:
            print('[-] Error generating diagram schema:', e)
            raise

    def _generate_namespace_schema(self, namespace: str) -> str:
        namespace_obj = self.resources_service.map_resources(namespace)
        namespace_diagram = str(namespace_obj)

        namespace_diagram += self._generate_relationships(namespace_obj)

        return namespace_diagram

    def _generate_relationships(self, namespace_obj: Namespace) -> str:
        relationships = '\n\n'

        for ingress in namespace_obj.ingresses:
            for service in ingress.services:
                relationships += (f'{service.name} -> {ingress.name}' + '\n')

        for service in namespace_obj.services:
            for deployment in service.deployments:
                relationships += (f'{deployment.name} -> {service.name}' + '\n')
            for pods in service.pods:
                relationships += (f'{pods.name} -> {service.name}' + '\n')

        for deployment in namespace_obj.deployments:
            for pod in deployment.pods:
                relationships += (f'{pod.name} -> {deployment.name}' + '\n')

        return relationships
        
        