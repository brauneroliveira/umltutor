from CommunicationDiagram import CommunicationDiagram

xmi = CommunicationDiagram('example.xml')

print(xmi.path)
print(xmi.tree)


print(xmi.getMessages())
