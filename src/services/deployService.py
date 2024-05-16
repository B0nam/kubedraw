class DeployService:
    def __init__(self, client):
        self.client = client
    
    def get_all(self):
        deploys = self.client.list_deployment_for_all_namespaces().items
        return [deploy.metadata.name for deploy in deploys]