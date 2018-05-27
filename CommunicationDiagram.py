from XmiFile import XmiFile

class CommunicationDiagram(XmiFile):

    def getLifelines(self):
        return self.tree.findall('.//lifeline')

    def getMessages(self):
        return self.tree.findall('.//message')