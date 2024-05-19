from kubernetes import config
from services.diagramService import DiagramService

def main():
    diagram_service = DiagramService()

    try:
        diagram_schema = diagram_service.generate_diagram_schema()
        print(diagram_schema)
    except Exception as e:
        print("[-] An error occurred:", e)

if __name__ == '__main__':
    main()