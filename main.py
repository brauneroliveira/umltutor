from CommunicationDiagram import CommunicationDiagram
from CommunicationDiagramComparator import CommunicationDiagramComparator
from MessageFlow import MessageFlow

left = CommunicationDiagram('PapyrusProject/UMLTutor/Student.uml')
right = CommunicationDiagram('PapyrusProject/UMLTutor/Oracle.uml')
comparator = CommunicationDiagramComparator(left, right)

print("=====")
print("Wrong format for Lifeline name: {}".format(comparator.validateLifelines()))
print("Correct Lifelines: {}".format(comparator.getCorrectLifelines()))
print("Missing Lifelines: {}".format(comparator.getMissingLifelines()))
print("Unnecessary Lifelines: {}".format(comparator.getUnnecessaryLifelines()))
print("=====")
print("Wrong format for Message name: {}".format(comparator.validateMessages()))
print("Correct Messages: {}".format(comparator.getCorrectMessages()))
print("Missing Messages: {}".format(comparator.getMissingMessages()))
print("Unnecessary Messages: {}".format(comparator.getUnnecessaryMessages()))
print("Correct Message flows: {}".format(comparator.getCorrectMessageFlows()))