from services.kubernetesService import KubernetesService
from models.namespaceModel import Namespace
from services.namespaceService import NamespaceService
from diagram.diagramGenerator import DiagramGenerator

class DiagramService:
    def __init__(self):
        self.kubernetes_service = KubernetesService()
        self.namespace_service = NamespaceService(self.kubernetes_service)

    def generate_diagram(self, namespace_name = 'None'):
        try:
            if namespace_name == 'None':
                all_namespaces = self.kubernetes_service.get_namespaces()
                for namespace in all_namespaces:
                    namespace_obj = self.namespace_service.generate_namespace_obj(namespace)
                    DiagramGenerator.generate_diagram(namespace_obj)
            else:
                namespace_obj = self.namespace_service.generate_namespace_obj(namespace_name)
                DiagramGenerator.generate_diagram(namespace_obj)
        except Exception as e:
            print("[-] An error occurred:", e)