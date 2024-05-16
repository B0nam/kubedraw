class NamespaceService:
    def __init__(self, client):
        self.client = client
    
    def get_all(self):
        namespaces = self.client.list_namespace().items
        return [namespace.metadata.name for namespace in namespaces]