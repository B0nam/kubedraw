from resources.models.namespaceModel import Namespace
from resources.models.deploymentModel import Deployment
from resources.models.podModel import Pod
from resources.models.serviceModel import Service
from resources.models.ingressModel import Ingress
from resources.services.kubernetesService import KubernetesService

class ResourceService:
    def __init__(self, kubernetes_service: KubernetesService):
        self.kubernetes_service = kubernetes_service

    def map_resources(self, namespace: str) -> Namespace:
        pods = self.kubernetes_service.list_pods(namespace)
        services = self.kubernetes_service.list_services(namespace)
        ingresses = self.kubernetes_service.list_ingresses(namespace)
        deployments = self.kubernetes_service.list_deployments(namespace)

        pod_objects = {pod.metadata.name: Pod(pod.metadata.name) for pod in pods}
        deployment_objects = {dep.metadata.name: Deployment(dep.metadata.name) for dep in deployments}
        service_objects = {svc.metadata.name: Service(svc.metadata.name) for svc in services}
        ingress_objects = {ing.metadata.name: Ingress(ing.metadata.name) for ing in ingresses}

        self._link_pods_to_deployments(deployments, deployment_objects, pods, pod_objects)
        self._link_services_to_deployments_and_pods(services, service_objects, deployments, deployment_objects, pods, pod_objects)
        self._link_services_to_ingresses(ingresses, ingress_objects, services, service_objects)

        return self._create_namespace_object(namespace, pod_objects, deployment_objects, service_objects, ingress_objects)

    def _link_pods_to_deployments(self, deployments: list, deployment_objects: dict, pods: list, pod_objects: dict):
        for dep in deployments:
            dep_obj = deployment_objects[dep.metadata.name]
            for pod_name in [pod.metadata.name for pod in pods if pod.metadata.owner_references and pod.metadata.owner_references[0].name == dep.metadata.name]:
                dep_obj.add_pod(pod_objects[pod_name])

    def _link_services_to_deployments_and_pods(self, services: list, service_objects: dict, deployments: list, deployment_objects: dict, pods: list, pod_objects: dict):
        for svc in services:
            svc_obj = service_objects[svc.metadata.name]
            selector = svc.spec.selector
            if selector:
                for dep in deployments:
                    dep_obj = deployment_objects[dep.metadata.name]
                    if all(item in dep.spec.selector.match_labels.items() for item in selector.items()):
                        svc_obj.add_deployment(dep_obj)
                for pod_name in [pod.metadata.name for pod in pods if all(item in pod.metadata.labels.items() for item in selector.items())]:
                    svc_obj.add_pod(pod_objects[pod_name])
    
    def _link_services_to_ingresses(self, ingresses: list, ingress_objects: dict, services: list, service_objects: dict):
        for ing in ingresses:
            ing_obj = ingress_objects[ing.metadata.name]
            for rule in ing.spec.rules:
                for path in rule.http.paths:
                    if path.backend.service:
                        service_name = path.backend.service.name
                        ing_obj.add_service(service_objects[service_name])

    def _create_namespace_object(self, namespace: str, pod_objects: dict, deployment_objects: dict, service_objects: dict, ingress_objects: dict) -> Namespace:
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