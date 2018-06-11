from XmiFile import XmiFile
from MessageFlow import MessageFlow
import re

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

    def getMessageFlows(self):
        messageNodes = self.getMessages()
        messageFlows = []
        for n in messageNodes:
            messageFlows.append(MessageFlow(
                self.getCoveredByLifeline(n.attrib['sendEvent']), 
                self.getCoveredByLifeline(n.attrib['receiveEvent']), 
                n.attrib['name']))
        return messageFlows

    def getCoveredByLifeline(self, xmid):
        lifelineNodes = self.getLifelines()
        for n in lifelineNodes:
            if re.search(xmid, n.attrib['coveredBy']):
                return n.attrib['name']
        return None