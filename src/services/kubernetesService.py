from kubernetes import client, config

class KubernetesService:
    def __init__(self):
        try:
            config.load_kube_config()
            print("[+] Kube-config loaded successfully.")
        except Exception as e:
            print("[-] Error loading kube-config file:", e)
            raise

        self.core_api = client.CoreV1Api()
        self.networking_api = client.NetworkingV1Api()
        self.apps_api = client.AppsV1Api()

    def get_namespaces(self) -> list:
        namespaces = self.core_api.list_namespace().items
        return [namespace.metadata.name for namespace in namespaces]

    def list_pods(self, namespace: str):
        return self.core_api.list_namespaced_pod(namespace).items

    def list_services(self, namespace: str):
        return self.core_api.list_namespaced_service(namespace).items

    def list_ingresses(self, namespace: str):
        return self.networking_api.list_namespaced_ingress(namespace).items

    def list_deployments(self, namespace: str):
        return self.apps_api.list_namespaced_deployment(namespace).items
