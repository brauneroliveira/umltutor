from CommunicationDiagram import CommunicationDiagram
from CommunicationDiagramComparator import CommunicationDiagramComparator
from MessageFlow import MessageFlow

left = CommunicationDiagram('PapyrusProject/UMLTutor/Student.uml')
right = CommunicationDiagram('PapyrusProject/UMLTutor/Oracle.uml')
comparator = CommunicationDiagramComparator(left, right)

wrongFlows = comparator.getWrongMessageFlows()

print(wrongFlows)

#print(MessageFlow(1, 2, 3) == MessageFlow(1, 22, 3))

#print(right.getMessageFlows())



# print(left.getMessages(False))
# print(comparator.validateLifelines())
# print(comparator.validateMessages())


#print(comparator.getMissingLifelines())
#print(comparator.getMissingMessages())


#print(left.getLifelines(False))