from diagram.diagramGenerator import DiagramGenerator
from services.diagramService import DiagramService
import sys

def main():
    diagram_service = DiagramService()

    try:
        if len(sys.argv) > 1:
            namespace = sys.argv[1]
            diagram_service.generate_diagram(namespace)
        else:
            diagram_service.generate_diagram()
    except Exception as e:
        print("[-] An error occurred:", e)

if __name__ == '__main__':
    main()
