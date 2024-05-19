from kubernetes import client, config
from models.namespaceModel import Namespace
from models.deploymentModel import Deployment
from models.podModel import Pod
from models.serviceModel import Service
from models.ingressModel import Ingress

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

    def map_resources(self, namespace: str) -> Namespace:
        pods = self.core_api.list_namespaced_pod(namespace)
        services = self.core_api.list_namespaced_service(namespace)
        ingresses = self.networking_api.list_namespaced_ingress(namespace)
        deployments = self.apps_api.list_namespaced_deployment(namespace)

        pod_objects = {pod.metadata.name: Pod(pod.metadata.name) for pod in pods.items}
        deployment_objects = {dep.metadata.name: Deployment(dep.metadata.name) for dep in deployments.items}
        service_objects = {svc.metadata.name: Service(svc.metadata.name) for svc in services.items}
        ingress_objects = {ing.metadata.name: Ingress(ing.metadata.name) for ing in ingresses.items}

        for dep in deployments.items:
            dep_obj = deployment_objects[dep.metadata.name]
            for pod_name in [pod.metadata.name for pod in pods.items if pod.metadata.owner_references and pod.metadata.owner_references[0].name == dep.metadata.name]:
                self.add_pod_to_deployment(dep_obj, pod_objects[pod_name])

        for svc in services.items:
            svc_obj = service_objects[svc.metadata.name]
            selector = svc.spec.selector
            if selector:
                for dep in deployments.items:
                    dep_obj = deployment_objects[dep.metadata.name]
                    if all(item in dep.spec.selector.match_labels.items() for item in selector.items()):
                        self.add_service_to_deployment(svc_obj, dep_obj)
                for pod_name in [pod.metadata.name for pod in pods.items if all(item in pod.metadata.labels.items() for item in selector.items())]:
                    self.add_pod_to_service(svc_obj, pod_objects[pod_name])

        for ing in ingresses.items:
            ing_obj = ingress_objects[ing.metadata.name]
            for rule in ing.spec.rules:
                for path in rule.http.paths:
                    if path.backend.service:
                        service_name = path.backend.service.name
                        self.add_service_to_ingress(ing_obj, service_objects[service_name])

        namespace_obj = Namespace(namespace)
        for pod in pod_objects.values():
            namespace_obj.add_pod(pod)
        for deploy in deployment_objects.values():
            namespace_obj.add_deployment(deploy)
        for service in service_objects.values():
            namespace_obj.add_service(service)
        for ingress in ingress_objects.values():
            namespace_obj.add_ingress(ingress)

        return namespace_obj

    def get_namespaces(self) -> list:
        namespaces = self.core_api.list_namespace().items
        return [namespace.metadata.name for namespace in namespaces]

    def add_pod_to_deployment(self, deployment: Deployment, pod: Pod):
        deployment.pods.append(pod)
        pod.deployment = deployment

    def add_service_to_deployment(self, service: Service, deployment: Deployment):
        service.deployment = deployment

    def add_pod_to_service(self, service: Service, pod: Pod):
        service.pods.append(pod)

    def add_service_to_ingress(self, ingress: Ingress, service: Service):
        ingress.services.append(service)