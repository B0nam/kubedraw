from diagrams import Diagram
from models.namespaceModel import Namespace
from diagrams.k8s.compute import Deployment, Pod
from diagrams.k8s.network import Ingress, Service

class DiagramGenerator:
    @staticmethod
    def generate_diagram(namespace: Namespace):
        with Diagram(f'Namespace: {namespace.name}', show=False, direction='BT'):
            pod_objs = {pod.name: Pod(pod.name) for pod in namespace.pods}
            deployment_objs = {deployment.name: Deployment(deployment.name) for deployment in namespace.deployments}
            service_objs = {service.name: Service(service.name) for service in namespace.services}
            ingress_objs = {ingress.name: Ingress(ingress.name) for ingress in namespace.ingresses}

            for deployment in namespace.deployments:
                for pod in deployment.pods:
                    if pod.name in pod_objs:
                        pod_objs[pod.name] >> deployment_objs[deployment.name]

            for service in namespace.services:
                for pod in service.pods:
                    if pod.name in pod_objs:
                        service_objs[service.name] >> pod_objs[pod.name]

            for ingress in namespace.ingresses:
                for service in ingress.services:
                    if service.name in service_objs:
                        ingress_objs[ingress.name] >> service_objs[service.name]