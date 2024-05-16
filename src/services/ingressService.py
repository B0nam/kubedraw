class IngressService:
    def __init__(self, client):
        self.client = client
    
    def get_all(self):
        ingresses = self.client.list_ingress_for_all_namespaces().items
        return [ingress.metadata.name for ingress in ingresses]