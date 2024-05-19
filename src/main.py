from diagram.diagramGenerator import DiagramGenerator
from resources.services.diagramService import DiagramService
import sys

def main():
    diagram_service = DiagramService()

    try:
        if len(sys.argv) > 1:
            namespace = sys.argv[1]
            namespace_obj = diagram_service.generate_namespace_obj(namespace)
            DiagramGenerator.generate_diagram(namespace_obj)
            diagram_schema = diagram_service.generate_diagram_schema(namespace)
            print(diagram_schema)
        else:
            diagram_schema = diagram_service.generate_diagram_schema()
            print(diagram_schema)
        
    except Exception as e:
        print("[-] An error occurred:", e)

if __name__ == '__main__':
    main()
