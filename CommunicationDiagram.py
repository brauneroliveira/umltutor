from XmiFile import XmiFile

class CommunicationDiagram(XmiFile):

    def getLifelines(self, asEtreenode=True):
        lifelineNodes = self.tree.findall('.//lifeline')
        if asEtreenode:
            return lifelineNodes
        else:
            lifelineNames = []
            for n in lifelineNodes:
                lifelineNames.append(n.attrib['name'])
            return lifelineNames


    def getMessages(self, asEtreenode=True):
        messageNodes = self.tree.findall('.//message')
        if asEtreenode:
            return messageNodes
        else:
            messageNames = []
            for n in messageNodes:
                messageNames.append(n.attrib['name'])
            return messageNames