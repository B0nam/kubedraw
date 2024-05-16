from kubernetes import client, config
from services.namespaceService import NamespaceService
from services.serviceService import ServiceService
from services.ingressService import IngressService
from services.deployService import DeployService

def set_kubernetes_client():
    global core_api, network_api
    try:
        config.load_kube_config()
    except Exception as e:
        print("Error trying to load kube-config file:", e)

def main():
    set_kubernetes_client()

    core_api = client.CoreV1Api()
    network_api = client.NetworkingV1Api()
    apps_api = client.AppsV1Api()

    if (core_api and network_api):
        namespace_service = NamespaceService(core_api)
        service_service = ServiceService(core_api)
        ingress_service = IngressService(network_api)
        deploy_service = DeployService(apps_api)

        print(namespace_service.get_all())
        print(service_service.get_all())
        print(ingress_service.get_all())
        print(deploy_service.get_all())

if __name__ == '__main__':
    main()