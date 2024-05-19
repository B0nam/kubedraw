from services.kubernetesService import KubernetesService

class DiagramService:
    def __init__(self):
        self.kubernetes_service = KubernetesService()
    
    def generate_diagram_schema(self) -> str:
        try:
            namespaces = self.kubernetes_service.get_namespaces()
            diagram_schema = ''
            for namespace in namespaces:
                namespace_obj = self.kubernetes_service.map_resources(namespace)
                diagram_schema += str(namespace_obj) + '\n\n'
            return diagram_schema
        except Exception as e:
            print("[-] Error generating diagram schema:", e)
            raise