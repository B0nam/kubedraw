class ServiceService:
    def __init__(self, client):
        self.client = client
    
    def get_all(self):
        services = self.client.list_service_for_all_namespaces().items
        return [service.metadata.name for service in services]