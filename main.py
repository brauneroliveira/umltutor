from CommunicationDiagram import CommunicationDiagram
from CommunicationDiagramComparator import CommunicationDiagramComparator

left = CommunicationDiagram('example2.xml')
right = CommunicationDiagram('example.xml')

comparator = CommunicationDiagramComparator(left, right)

print(comparator.getMissingLifelines())

